from odmantic import query

from src.database.connection import DbConnectionHandler
from src.game.repository import GameRepository
from src.game.models import GameModel

from .repository import QuestionRepository
from . import schemas


class CreateQuestionUseCase:
    def __init__(self, context: DbConnectionHandler, payload: schemas.Question, game_id: int) -> None:
        self._repository = QuestionRepository(context)
        self._game_repository = GameRepository(context)
        self._payload = payload
        self._game_id = game_id

    async def execute(self):
        game = self._game_repository.get(
            query.eq(self._game_id, GameModel.id)
        )

        return self._repository.create(
            schemas.ExtendedQuestion(
                name=self._payload.name,
                question_type=self._payload.question_type,
                choices=self._payload.choices,
                game=game,
                point_value=self._payload.point_value
            )
        )
