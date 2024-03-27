from fastapi import APIRouter, Body, Depends

from src.api import dependencies
from src.database.connection import DbConnectionHandler
from src.common.user import User, ExtendedUser
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


@router.patch("/", status_code=204)
async def update_information(
    context: DbConnectionHandler = Depends(
        dependencies.get_database_connection),
    user: ExtendedUser = Depends(protected_route),
    payload: schemas.UpdateUserPayload = Body(...)
):
    return await domain.UpdateUserUseCase(context, user, payload).execute()


@router.delete("/", status_code=204)
async def delete_self_user(
    context: DbConnectionHandler = Depends(
        dependencies.get_database_connection),
    user: ExtendedUser = Depends(protected_route)
):
    return await domain.DeleteSelfUserUseCase(context, user).execute()
