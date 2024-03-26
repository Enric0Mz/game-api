from fastapi import APIRouter, Body, Depends

from src.api import dependencies
from src.database.connection import DbConnectionHandler
from src.common.user import User
from src.auth.domain import protected_route

from . import domain, schemas

router = APIRouter(dependencies=[Depends(protected_route)])


@router.get("/me", response_model=schemas.UserPayload)
async def get_me(
    context: DbConnectionHandler = Depends(
        dependencies.get_database_connection),
    user: User = Depends(protected_route)
):
    return await domain.GetUserMeUseCase(context, user).execute()
