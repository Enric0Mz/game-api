import random

from odmantic import query
from odmantic import ObjectId

from src.database.connection import DbConnectionHandler
from src.game.repository import GameRepository
from src.game.models import GameModel

from .repository import QuestionRepository
from .models import QuestionModel
from . import schemas


class ListQuestionUseCase:
    def __init__(self, context: DbConnectionHandler, game_id: int) -> None:
        self._repository = QuestionRepository(context)
        self._game_id = game_id

    async def execute(self):
        result = await self._repository.fetch(query.eq(QuestionModel.game.id_, ObjectId(self._game_id)))
        return {"data": result}
    

class GetRandomQuestionUseCase:
    def __init__(self, context: DbConnectionHandler, game_id: int) -> None:
        self._repository = QuestionRepository(context)
        self._game_id = game_id

    async def execute(self):
        questions = await self._repository.fetch(query.eq(QuestionModel.game.id_, ObjectId(self._game_id)))

        return random.choice(questions)


class CreateQuestionUseCase:
    def __init__(self, context: DbConnectionHandler, payload: schemas.Question, game_id: int) -> None:
        self._repository = QuestionRepository(context)
        self._game_repository = GameRepository(context)
        self._payload = payload
        self._game_id = game_id

    async def execute(self):
        game = await self._game_repository.get(
            query.eq(GameModel.id, ObjectId(self._game_id))
        )
        return await self._repository.create(
            schemas.ExtendedQuestion(
                name=self._payload.name,
                question_type=self._payload.question_type,
                choices=self._payload.choices,
                game=game,
                point_value=self._payload.point_value
            )
        )
