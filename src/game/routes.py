from fastapi import APIRouter
from fastapi import Depends
from fastapi import Body

from src.database.connection import DbConnectionHandler
from src.api import dependencies
from src.common.result import ListResult

from . import domain
from . import schemas


router = APIRouter()


@router.get("/", response_model=ListResult[schemas.ExtendedGame])
async def list_game(
    context: DbConnectionHandler = Depends(
        dependencies.get_database_connection)
):
    return await domain.ListGameUseCase(context).execute()



@router.post("/", response_model=schemas.Game)
async def crete_game(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    payload: schemas.Game = Body(...)
):
    return await domain.CreateGameUseCase(context, payload).execute()