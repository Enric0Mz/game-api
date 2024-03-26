from datetime import datetime, timedelta, timezone
import jwt

from fastapi.security import OAuth2PasswordRequestForm
from odmantic import query

from src.api import exc
from src.api.security.password import verify_password
from src.api.security.tokens import create_token
from src.core.settings import ACCESS_TOKEN_EXPIRES, REFRESH_TOKEN_EXPIRES
from src.core.settings import SECRET_KEY, ALGORITHM
from src.database.connection import DbConnectionHandler
from src.user.models import UserModel
from src.user.repository import UserRepository
from src.user.schemas import User


from .models import TokenModel
from . import schemas
from .repository import AuthRepository


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


def _create_tokens(user: User):
    access_token = create_token(
        {"sub": user.email}, timedelta(minutes=ACCESS_TOKEN_EXPIRES)
    )
    refresh_token = create_token(
        {"sub": user.nickname}, timedelta(days=REFRESH_TOKEN_EXPIRES)
    )
    return access_token, refresh_token
