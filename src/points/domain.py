from odmantic import query

from src.database.connection import DbConnectionHandler
from src.common.page import PaginationParams

from .repository import PointRepository
from .models import PointModel
from . import schemas


class ListUserPointsUseCase:
    def __init__(self, context: DbConnectionHandler, params: PaginationParams) -> None:
        self._repository = PointRepository(context)
        self._params = params


    async def execute(self):
        return {"data": await self._repository.fetch()} # TODO add user query later
    