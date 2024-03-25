from fastapi import APIRouter
from fastapi import Depends
from fastapi import Body

from src.database.connection import DbConnectionHandler
from src.api import dependencies

from . import domain
from . import schemas


router = APIRouter()


@router.post("/", status_code=204)
async def create_user(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    payload: schemas.User = Body(...)
):
    await domain.CreateUserUseCase(context, payload).execute()
