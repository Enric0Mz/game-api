from datetime import datetime

from odmantic import ObjectId, query

from src.database.connection import DbConnectionHandler
from src.points.repository import PointRepository
from src.points.schemas import ExtendedPoint
from src.question.models import QuestionModel
from src.question.repository import QuestionRepository

from . import schemas
from .repository import AnswerRepository


class CreateAnswerUseCase:
    def __init__(
        self, context: DbConnectionHandler, question_id: str, choice_id: str
    ) -> None:
        self._repository = AnswerRepository(context)
        self._question_repository = QuestionRepository(context)
        self._point_repository = PointRepository(context)
        self._question_id = question_id
        self._choice_id = choice_id

    async def execute(self):
        question = await self._question_repository.get(
            query.eq(QuestionModel.id, ObjectId(self._question_id))
        )
        choice = None
        for obj in question.choices:
            if ObjectId(self._choice_id) == ObjectId(obj.id_):
                choice = obj
            if obj.correct:
                correct = obj
                break

        answer = await self._repository.create(
            schemas.Answer(
                created_at=datetime.utcnow(), choice=choice, question=question
            )
        )

        await self._process_points(question, choice, correct, answer)

    async def _process_points(
        self,
        question: schemas.Question,
        choice: schemas.Choice,
        correct: schemas.Choice,
        answer: schemas.Answer,
    ) -> None:
        if choice == correct:
            points_total = (
                question.point_value * question.question_type.point_multiplier
            )
            await self._point_repository.create(
                ExtendedPoint(
                    created_at=datetime.utcnow(), total=points_total, answer=answer
                )
            )
        else:
            await self._point_repository.create(
                ExtendedPoint(created_at=datetime.utcnow(), total=0, answer=answer)
            )
