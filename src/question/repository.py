from odmantic.query import QueryExpression

from src.database.repository import Repository

from .models import QuestionModel
from . import schemas


class QuestionRepository(Repository):
    def to_dto(self, obj: QuestionModel) -> schemas.Question:
        return schemas.Question.model_validate(
            {
                "name": obj.name,
                "choices": [choice for choice in obj.choices],
                "question_type": obj.question_type,
                "game": obj.game,
                "poin_value": obj.point_value
            }
        )