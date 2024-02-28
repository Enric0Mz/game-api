from .connection import DbConnectionHandler

from src.game.models import GameModel

engine = DbConnectionHandler()


async def database_config():
    await engine.acquire_session().configure_database(
        [GameModel],
        update_existing_indexes=True,
    )
