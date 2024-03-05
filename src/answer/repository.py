from src.database.repository import Repository

from .models import AnswerModel
from . import schemas


class AnswerRepository(Repository):
    def to_dto(self, obj: AnswerModel) -> schemas.Answer:
        return schemas.Answer.model_validate(
            {
                "user_id": obj.user_id,
                "created_at": obj.created_at,
                "choice": obj.choice,
                "question": obj.question
            }
        )