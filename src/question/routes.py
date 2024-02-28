from fastapi import APIRouter
from fastapi import Path
from fastapi import Depends
from fastapi import Body

from src.api import dependencies
from src.database.connection import DbConnectionHandler

from . import domain
from . import schemas


router = APIRouter()


@router.post("/{game_id}", response_model=schemas.ExtendedQuestion)
async def create_question(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    payload: schemas.Question = Body(...), 
    game_id: str = Path(...)
):
    domain.CreateQuestionUseCase(context, payload, game_id).execute()
