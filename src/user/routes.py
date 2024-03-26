from fastapi import APIRouter, Body, Depends

from src.api import dependencies
from src.database.connection import DbConnectionHandler

from . import domain, schemas

from src.auth.domain import protected_route

router = APIRouter(dependencies=[Depends(protected_route)])
