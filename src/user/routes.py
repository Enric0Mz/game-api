from fastapi import APIRouter, Body, Depends

from src.api import dependencies
from src.database.connection import DbConnectionHandler

from . import domain, schemas

router = APIRouter()


@router.post("/", status_code=204)
async def create_user(
    context: DbConnectionHandler = Depends(dependencies.get_database_connection),
    payload: schemas.User = Body(...),
):
    await domain.CreateUserUseCase(context, payload).execute()
