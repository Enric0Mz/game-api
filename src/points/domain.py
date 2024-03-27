from odmantic import query

from src.common.page import PaginationParams
from src.database.connection import DbConnectionHandler
from src.common.user import ExtendedUser

from . import schemas
from .models import PointModel
from .repository import PointRepository


class ListUserPointsUseCase:
    def __init__(self, context: DbConnectionHandler, params: PaginationParams, user: ExtendedUser) -> None:
        self._repository = PointRepository(context)
        self._params = params
        self._user = user

    async def execute(self):
        return {"data": await self._repository.fetch(query.eq(PointModel.answer.user_id, self._user.id))}