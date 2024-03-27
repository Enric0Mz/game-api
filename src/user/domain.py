from odmantic import query

from src.common.user import ExtendedUser
from src.database.connection import DbConnectionHandler
from src.api import exc
from src.api.security.password import get_password_hash, verify_password

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
        user = await self._repository.get(
            query.eq(UserModel.id, self._user.id)
        )
        verify = verify_password(self._payload.current.password, user.password)
        if not verify:
            return exc.incorrect_password_exception()
        if self._payload.password != self._payload.confirm_password:
            raise exc.unmatch_passwords_exception()

        if self._payload.password:
            hashed_password = get_password_hash(self._payload.password)

        await self._repository.update(query.eq(UserModel.id, self._user.id),
            schemas.UpdateUser(
                nickname=self._payload.nickname,
                password=hashed_password if hashed_password else None
            )
        )
