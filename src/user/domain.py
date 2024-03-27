from odmantic import query

from src.common.user import ExtendedUser
from src.database.connection import DbConnectionHandler
from src.api import exc

from .models import UserModel
from .repository import UserRepository
from . import schemas


class GetUserMeUseCase:
    def __init__(self, context: DbConnectionHandler, user: ExtendedUser) -> None:
        self._repository = UserRepository(context)
        self._user = user

    async def execute(self):
        return await self._repository.get(
            query.eq(UserModel.id, self._user.id)
        )


class UpdateUserUseCase:
    def __init__(self, context: DbConnectionHandler, user: ExtendedUser, payload: schemas.UpdateUserPayload) -> None:
        self._repository = UserRepository(context)
        self._user = user
        self._payload = payload

    async def execute(self):
        user = self._repository.get(query.and_(
            query.eq(UserModel.id, self._user.id),
            query.eq(UserModel.password, self._payload.current.password)
        ))

        if not user:
            return exc.incorrect_password_exception()
        if self._payload.password != self._payload.confirm_password:
            raise exc.incorrect_password_exception()
        await self._repository.update(
            schemas.UpdateUser(
                nickname=self._payload.nickname,
                password=self._payload.password
            )
        )