from src.database.connection import DbConnectionHandler

from .repository import UserRepository
from .models import UserModel
from . import schemas


class CreateUserUseCase:
    def __init__(self, context: DbConnectionHandler, payload: schemas.User) -> None:
        self._repository = UserRepository(context)
        self._payload = payload

    async def execute(self):
        ...