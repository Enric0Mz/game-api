from odmantic import query
from datetime import datetime
from odmantic import ObjectId

from src.database.connection import DbConnectionHandler
from src.question.repository import QuestionRepository
from src.question.models import QuestionModel

from .repository import AnswerRepository
from . import schemas


class CreateAnswerUseCase:
    def __init__(self, context: DbConnectionHandler, question_id: str, choice_id: str) -> None:
        self._repository = AnswerRepository(context)
        self._question_repository = QuestionRepository(context)
        self._question_id = question_id
        self._choice_id = choice_id

    async def execute(self):
        question = await self._question_repository.get(query.eq(QuestionModel.id, ObjectId(self._question_id)))
        choice = None
        for obj in question.choices:
            if ObjectId(self._choice_id) == ObjectId(obj.id_):
                choice = obj

        return await self._repository.create(schemas.Answer(
                created_at=datetime.utcnow(),
                choice=choice,
                question=question
            ))
