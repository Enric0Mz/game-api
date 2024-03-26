from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from odmantic import query

from src.api import exc
from src.api.security.password import verify_password
from src.api.security.tokens import create_token
from src.core.settings import ACCESS_TOKEN_EXPIRES, REFRESH_TOKEN_EXPIRES
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
        self._access_expires = ACCESS_TOKEN_EXPIRES
        self._refresh_expires = REFRESH_TOKEN_EXPIRES

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
                created_at=datetime.utcnow(),
            )
        )
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }

    def _validate_user(self, user: User):
        if not user:
            return exc.not_found_exception(self._payload.username, "User")
        if not verify_password(self._payload.password, user.password):
            return exc.incorrect_password_exception()

class GetRefreshTokenUseCase:
    def __init__(self, context: DbConnectionHandler, access_token: str) -> None:
        self._repository = AuthRepository(context)
        self._user_repository = UserRepository(context)
        self._access_token = access_token

    async def execute(self):
        exists = await self._repository.get(
            query.eq(TokenModel.access_token, self._access_token)
        )
        if not exists:
            return exc.not_found_exception("token", "Token") # Change to expire or invalid token exc
    
        user = await self._user_repository.get(query.eq(UserModel.id, exists.user_id))
        access_token, refresh_token = _create_tokens(user)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
        

def _create_tokens(self, user: User):
        access_token = create_token(
            {"sub": user.email}, timedelta(minutes=self._access_expires)
        )
        refresh_token = create_token(
            {"sub": user.nickname}, timedelta(days=self._refresh_expires)
        )
        return access_token, refresh_token
