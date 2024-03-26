from fastapi import APIRouter, Body, Depends

from src.api import dependencies
from src.common.result import ListResult
from src.database.connection import DbConnectionHandler
from src.auth.domain import protected_route

from . import domain, schemas

router = APIRouter(dependencies=[Depends(protected_route)])


@router.get("/", response_model=ListResult[schemas.ExtendedGame])
async def list_game(
    context: DbConnectionHandler = Depends(
        dependencies.get_database_connection),
):
    return await domain.ListGameUseCase(context).execute()


@router.post("/", response_model=schemas.Game)
async def crete_game(
    context: DbConnectionHandler = Depends(
        dependencies.get_database_connection),
    payload: schemas.Game = Body(...),
):
    return await domain.CreateGameUseCase(context, payload).execute()
