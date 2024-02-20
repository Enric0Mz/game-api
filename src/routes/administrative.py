from fastapi import APIRouter
from fastapi import Depends
from fastapi import Body

from src.database.connection import DbConnectionHandler
from src.api import dependencies
from src.domain import game
from src import schemas

router = APIRouter()


@router.post("/game", response_model=schemas.Game)
async def crete_game(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    payload: schemas.Game = Body(...)
):
    return await game.CreateGameUseCase(context, payload).execute()
