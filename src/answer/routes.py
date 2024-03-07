from fastapi import APIRouter
from fastapi import Path
from fastapi import Query
from fastapi import Depends

from src.api import dependencies
from src.database.connection import DbConnectionHandler

from . import domain


router = APIRouter()


@router.post("/{question_id}", status_code=204)
async def create_answer(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    question_id: str = Path(...),
    choice_id: str = Query(...)
):
    await domain.CreateAnswerUseCase(context, question_id, choice_id).execute()
