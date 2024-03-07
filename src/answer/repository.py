from odmantic.query import QueryExpression

from src.database.repository import Repository

from . import schemas
from .models import AnswerModel


class AnswerRepository(Repository):
    def to_dto(self, obj: AnswerModel):
        return schemas.Answer.model_validate(
            {
                "id": obj.id,
                "created_at": obj.created_at,
                "choice": obj.choice,
                "question": obj.question
            }
        )



    async def create(self, payload: schemas.Answer):
        obj = await self.context.acquire_session().save(AnswerModel(**payload.model_dump()))
        return self.to_dto(obj)
