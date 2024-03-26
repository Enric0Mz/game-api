from fastapi import APIRouter, Depends
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm

from src.api import dependencies
from .domain import protected_route
from src.database.connection import DbConnectionHandler
from src.common.user import User

from . import domain
from . import schemas

router = APIRouter()


@router.post("/user", status_code=204)
async def create_user(
    context: DbConnectionHandler = Depends(
        dependencies.get_database_connection),
    payload: User = Body(...),
):
    await domain.CreateUserUseCase(context, payload).execute()


@router.post("/token")
async def authenticate(
    context: DbConnectionHandler = Depends(
        dependencies.get_database_connection),
    payload: OAuth2PasswordRequestForm = Depends(),
):
    return await domain.UserAuthenticateUseCase(context, payload).execute()


@router.post("/token/refresh")
async def get_refresh_token(
    context: DbConnectionHandler = Depends(
        dependencies.get_database_connection),
    refresh_token_payload: schemas.TokenPayload = Body(
        ..., alias="refresh_token"),
    user: User = Depends(protected_route)
):
    return await domain.GetRefreshTokenUseCase(context, refresh_token_payload, user).execute()


@router.delete("/token/logout", status_code=204)
async def user_logout(
    context: DbConnectionHandler = Depends(
        dependencies.get_database_connection),
    user: User = Depends(protected_route)
):
    await domain.LogOutUseCase(context, user).execute()
