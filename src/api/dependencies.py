from fastapi import Request

from src.database.connection import DbConnectionHandler


def get_database_connection(request: Request) -> None:
    return DbConnectionHandler()
