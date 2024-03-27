from fastapi import APIRouter, Depends

from src.api import dependencies
from src.common.page import PaginationParams
from src.common.result import ListResult
from src.database.connection import DbConnectionHandler
from src.auth.domain import protected_route
from src.common.user import ExtendedUser

from . import domain, schemas

router = APIRouter(dependencies=[Depends(protected_route)])


@router.get("/", response_model=ListResult[schemas.PointPayload])
async def list_user_points(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    params: PaginationParams = Depends(),
    user: ExtendedUser = Depends(protected_route)
):
    return await domain.ListUserPointsUseCase(context, params, user).execute()
