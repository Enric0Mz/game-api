from src.api.security.password import get_password_hash
from src.database.connection import DbConnectionHandler

from . import schemas
from .models import UserModel
from .repository import UserRepository


class CreateUserUseCase:
    def __init__(self, context: DbConnectionHandler, payload: schemas.User) -> None:
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
