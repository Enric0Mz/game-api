from fastapi import APIRouter, Body, Depends, Path

from src.api import dependencies
from src.common.result import ListResult
from src.database.connection import DbConnectionHandler
from src.auth.domain import protected_route

from . import domain, schemas

router = APIRouter(dependencies=[Depends(protected_route)])


@router.get("/{game_id}", response_model=ListResult[schemas.Question])
async def list_question(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    game_id: str = Path(...),
):
    return await domain.ListQuestionUseCase(context, game_id).execute()


@router.get("/random/{game_id}", response_model=schemas.Question)
async def get_random_question(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    game_id: str = Path(...),
):
    return await domain.GetRandomQuestionUseCase(context, game_id).execute()


@router.post("/{game_id}", status_code=204)
async def create_question(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    payload: schemas.QuestionPayload = Body(...),
    game_id: str = Path(...),
):
    return await domain.CreateQuestionUseCase(context, payload, game_id).execute()
