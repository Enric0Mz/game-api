import jwt
from datetime import datetime, timedelta, timezone
from fastapi import Request
from fastapi import Depends
from fastapi.requests import Request
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials

from fastapi.security import OAuth2PasswordRequestForm
from odmantic import query

from src.api import exc
from src.api.security.password import verify_password, get_password_hash
from src.api.security.tokens import create_token
from src.core.settings import ACCESS_TOKEN_EXPIRES, REFRESH_TOKEN_EXPIRES
from src.core.settings import SECRET_KEY, ALGORITHM
from src.database.connection import DbConnectionHandler
from src.common.user import User

from src.api.dependencies import get_database_connection

from .models import TokenModel
from .models import UserModel
from . import schemas
from .repository import AuthRepository
from .repository import UserRepository


class UserAuthenticateUseCase:
    def __init__(
        self, context: DbConnectionHandler, payload: OAuth2PasswordRequestForm
    ) -> None:
        self._payload = payload
        self._repository = AuthRepository(context)
        self._user_repository = UserRepository(context)

    async def execute(self):
        user = await self._user_repository.get(
            query.eq(UserModel.email, self._payload.username)
        )
        self._validate_user(user)
        access_token, refresh_token = _create_tokens(user)
        await self._repository.update(
            schemas.Token(
                user_id=user.id,
                access_token=access_token,
                refresh_token=refresh_token,
                created_at=datetime.now(timezone.utc),
            )
        )
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }

    def _validate_user(self, user: User):
        if not user:
            return exc.not_found_exception("email", self._payload.username)
        if not verify_password(self._payload.password, user.password):
            return exc.incorrect_password_exception()


class GetRefreshTokenUseCase:
    def __init__(self, context: DbConnectionHandler, refresh_token_payload: schemas.TokenPayload, user: User) -> None:
        self._repository = AuthRepository(context)
        self._user_repository = UserRepository(context)
        self._refresh_token = refresh_token_payload.refresh_token
        self._user = user

    async def execute(self):
        try:
            decoded_token = jwt.decode(
                self._refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.DecodeError:
            return exc.invalid_token_exception("Invalid or expired refresh token")
        if not decoded_token:
            return exc.invalid_token_exception("Invalid or expired refresh token")
        exists = await self._repository.get(
            query.eq(TokenModel.refresh_token, self._refresh_token)
        )
        if not exists:
            return exc.invalid_token_exception("Invalid or expired refresh token")

        access_token, refresh_token = _create_tokens(self._user)
        await self._repository.update(
            schemas.Token(
                user_id=self._user.id,
                access_token=access_token,
                refresh_token=refresh_token,
                created_at=datetime.now(timezone.utc),
            )
        )
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }


class LogOutUseCase:
    def __init__(self, context: DbConnectionHandler, user: User) -> None:
        self._repository = AuthRepository(context)
        self._user = user

    async def execute(self):
        print(self._user)
        await self._repository.delete(
            query.eq(TokenModel.user_id, self._user.id)
        )


class CreateUserUseCase:
    def __init__(self, context: DbConnectionHandler, payload: User) -> None:
        self._repository = UserRepository(context)
        self._payload = payload

    async def execute(self):
        await self._repository.create(
            schemas.User(
                nickname=self._payload.nickname,
                email=self._payload.email,
                password=get_password_hash(self._payload.password),
            )
        )



class AuthValidator(HTTPBearer):
    def __init__(self, context: DbConnectionHandler, auto_error: bool = False):
        self._repository = AuthRepository(context)
        self._user_repository = UserRepository(context)
        super(AuthValidator, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(AuthValidator, self).__call__(request)

        if not credentials:
            return exc.invalid_token_exception("User not authenticated")
        if not credentials.scheme == "Bearer":
            return exc.invalid_token_exception("Invalid token type")
        token_payload = await self.verify_jwt(credentials.credentials)
        user = await self._user_repository.get(query.eq(UserModel.id, token_payload.user_id))
        if not user:
            return exc.invalid_token_exception("Invalid or expired token")
        return user

    async def verify_jwt(self, token: str):
        try:
            jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except:
            return exc.invalid_token_exception("Invalid or expired Token")
        exists = await self._repository.get(
            query.eq(TokenModel.access_token, token))
        if not exists:
            return exc.invalid_token_exception("Invalid or Expired Token")
        return exists


async def protected_route(user=Depends(AuthValidator(get_database_connection(Request)))):
    return user


def _create_tokens(user: User):
    access_token = create_token(
        {"sub": user.email}, timedelta(minutes=ACCESS_TOKEN_EXPIRES)
    )
    refresh_token = create_token(
        {"sub": user.nickname}, timedelta(days=REFRESH_TOKEN_EXPIRES)
    )
    return access_token, refresh_token
