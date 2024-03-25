from src.game.models import GameModel
from src.user.models import UserModel


from .connection import DbConnectionHandler

engine = DbConnectionHandler()


async def database_config():
    await engine.acquire_session().configure_database(
        [GameModel, UserModel],
        update_existing_indexes=True,
    )
