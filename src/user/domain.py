from odmantic import query

from src.common.user import ExtendedUser
from src.database.connection import DbConnectionHandler

from .models import UserModel
from .repository import UserRepository


class GetUserMeUseCase:
    def __init__(self, context: DbConnectionHandler, user: ExtendedUser) -> None:
        self._repository = UserRepository(context)
        self._user = user

    async def execute(self):
        return await self._repository.get(
            query.eq(UserModel.id, self._user.id)
        )
