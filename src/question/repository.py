from odmantic.query import QueryExpression

from src.database.repository import Repository

from .models import QuestionModel
from . import schemas


class QuestionRepository(Repository):
    def to_dto(self, obj: QuestionModel) -> schemas.ExtendedQuestion:
        return schemas.ExtendedQuestion.model_validate(
            {
                "name": obj.name,
                "choices": [choice for choice in obj.choices],
                "question_type": obj.question_type,
                "game": obj.game,
                "poin_value": obj.point_value
            }
        )
    
    async def fetch(self, clause: QueryExpression):
        result = await self.context.acquire_session().find(QuestionModel, clause)
        return [self.to_dto(obj) for obj in result]

    async def create(self, payload: schemas.ExtendedQuestion):
        result = self.context.acquire_session().save(QuestionModel(**payload.model_dump()))
        return self.to_dto(result)
