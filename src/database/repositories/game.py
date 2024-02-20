from src.models.game import GameModel

from .repository import Repository


class GameRepository(Repository):
    def to_dto(obj: GameModel):
        ...


    async def crete(self, payload) -> None:
        result = await self.context.acquire_session().save(GameModel(**payload))
        return self.to_dto(result)
