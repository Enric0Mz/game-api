from fastapi import APIRouter
from fastapi import Path
from fastapi import Depends
from fastapi import Body

from src.api import dependencies
from src.database.connection import DbConnectionHandler
from src.common.result import ListResult

from . import domain
from . import schemas


router = APIRouter()


@router.get("/{game_id}", response_model=ListResult[schemas.Question])
async def list_question(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    game_id: str = Path(...)
):
    return await domain.ListQuestionUseCase(context, game_id).execute()


@router.post("/{game_id}", status_code=204)
async def create_question(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    payload: schemas.Question = Body(...), 
    game_id: str = Path(...)
):
    return await domain.CreateQuestionUseCase(context, payload, game_id).execute()
