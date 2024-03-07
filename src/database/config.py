from src.game.models import GameModel

from .connection import DbConnectionHandler

engine = DbConnectionHandler()


async def database_config():
    await engine.acquire_session().configure_database(
        [GameModel],
        update_existing_indexes=True,
    )
