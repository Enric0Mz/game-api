import jwt

from fastapi import Request
from fastapi import Depends
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from odmantic import query

from src.core.settings import ALGORITHM, SECRET_KEY
from src.database.connection import DbConnectionHandler
from src.auth.repository import AuthRepository
from src.user.repository import UserRepository
from src.auth.models import TokenModel
from src.user.models import UserModel
from src.api.dependencies import get_database_connection

from src.api import exc


class AuthValidator(HTTPBearer):
    def __init__(self, context: DbConnectionHandler, auto_error: bool = False):
        self._repository = AuthRepository(context)
        self._user_repository = UserRepository(context)
        super(AuthValidator, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(AuthValidator, self).__call__(request)

        if not credentials:
            return exc.invalid_token_exception("Invalid auth Token")
        if not credentials.scheme == "Bearer":
            return exc.invalid_token_exception("Invalid token type")
        token_payload = self.verify_jwt(credentials.credentials)
        user = await self._user_repository.get(query.eq(UserModel.id, token_payload.user_id))
        if not user:
            return exc.invalid_token_exception("Invalid or expired token")
        return user

    def verify_jwt(self, token: str):
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except:
            return exc.invalid_token_exception("Invalid or expired Token")
        exists = self._repository.get(query.eq(TokenModel.access_token, decoded))
        if not exists:
            return exc.invalid_token_exception("Invalid or Expired Token")
        return exists


def protected_route():
    return AuthValidator(Depends(get_database_connection))