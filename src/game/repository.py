from odmantic.query import QueryExpression

from src.game.models import GameModel
from src.game import schemas

from src.database.repository import Repository


class GameRepository(Repository):
    def to_dto(self, obj: GameModel) -> schemas.Game:
        return schemas.Game.model_validate(
            {
                "id": obj.id,
                "subject": obj.subject,
                "start_at": obj.start_at,
                "finish_at": obj.finish_at
            }
        )

    async def fetch(self, clause: QueryExpression):
        result = await self.context.acquire_session().find(GameModel, clause)
        return [self.to_dto(obj) for obj in result]
    
    async def get(self, clause: QueryExpression):
        result = await self.context.acquire_session().find_one(GameModel, clause)
        if first := result:
            return self.to_dto(first)
        raise "NOT FOUND ERROR" #TODO make correct exception        

    async def create(self, payload: schemas.CreateGame) -> schemas.Game:
        result = await self.context.acquire_session().save(GameModel(**payload.model_dump()))
        return self.to_dto(result)
