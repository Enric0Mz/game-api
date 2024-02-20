from src.models.game import GameModel
from src import schemas

from .repository import Repository


class GameRepository(Repository):
    def to_dto(self, obj: GameModel) -> schemas.Game:
        return schemas.Game.model_validate(
            {
                "subject": obj.subject,
                "start_at": obj.start_at,
                "finish_at": obj.finish_at
            }
        )

    async def create(self, payload: schemas.CreateGame) -> schemas.Game:
        result = await self.context.acquire_session().save(GameModel(**payload.model_dump()))
        return self.to_dto(result)
