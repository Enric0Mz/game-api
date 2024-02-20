from datetime import datetime

from src.database.connection import DbConnectionHandler
from src.database.repositories.game import GameRepository

from src import models
from src import schemas


class CreateGameUseCase:
    def __init__(self, context: DbConnectionHandler, payload: schemas.Game) -> None:
        self._repository = GameRepository(context)
        self._payload = payload

    async def execute(self):
        curdate = datetime.utcnow()
        return await self._repository.create(
            schemas.CreateGame(
                subject=self._payload.subject,
                created_at=curdate,
                start_at=self._payload.start_at,
                finish_at=self._payload.finish_at,
            )
        )
