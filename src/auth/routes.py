from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.database.connection import DbConnectionHandler
from src.api import dependencies

from . import domain


router = APIRouter()


@router.post("/token")
async def authenticate(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    payload: OAuth2PasswordRequestForm = Depends()
):
    return await domain.UserAuthenticateUseCase(context, payload).execute()