from fastapi import APIRouter
from fastapi import Depends

from src.database.connection import DbConnectionHandler
from src.api import dependencies
from src.domain import game
from src import schemas

router = APIRouter()


@router.get("/", response_model=list[schemas.Game]
            )
async def list_game(
    context: DbConnectionHandler = Depends(
        dependencies.get_database_connection)
):
    return await game.ListGameUseCase(context).execute()
