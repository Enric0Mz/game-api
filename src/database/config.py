from .connection import DbConnectionHandler

from src import models

engine = DbConnectionHandler()


async def database_config():
    await engine.acquire_session().configure_database(
        [],
        update_existing_indexes=True,
    )
