from fastapi import APIRouter
from fastapi import Depends

from src.database.connection import DbConnectionHandler
from src.api import dependencies
from src.common.page import PaginationParams
from src.common.result import ListResult

from . import schemas
from . import domain


router = APIRouter()


@router.get("/", response_model=ListResult[schemas.PointPayload])
async def list_user_points(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    params: PaginationParams = Depends()
):
    return await domain.ListUserPointsUseCase(context, params).execute()