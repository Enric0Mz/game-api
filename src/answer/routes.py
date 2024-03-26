from fastapi import APIRouter, Depends, Path, Query

from src.api import dependencies
from src.database.connection import DbConnectionHandler
from src.auth.domain import protected_route

from . import domain

router = APIRouter(dependencies=[Depends(protected_route)])


@router.post("/{question_id}", status_code=204)
async def create_answer(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    question_id: str = Path(...),
    choice_id: str = Query(...),
):
    await domain.CreateAnswerUseCase(context, question_id, choice_id).execute()
