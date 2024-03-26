from fastapi import APIRouter, Depends
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm

from src.api import dependencies
from src.database.connection import DbConnectionHandler

from . import domain
from . import schemas

router = APIRouter()


@router.post("/token")
async def authenticate(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    payload: OAuth2PasswordRequestForm = Depends(),
):
    return await domain.UserAuthenticateUseCase(context, payload).execute()


@router.post("/token/refresh")
async def get_refresh_token(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    refresh_token_payload: schemas.TokenPayload = Body(..., alias="refresh_token"),
):
    return await domain.GetRefreshTokenUseCase(context, refresh_token_payload).execute()
