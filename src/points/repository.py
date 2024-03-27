from odmantic.query import QueryExpression

from src.database.repository import Repository

from . import schemas
from .models import PointModel


class PointRepository(Repository):
    def to_dto(self, obj: PointModel) -> schemas.PointPayload:
        return schemas.PointPayload.model_validate(
            {
                "created_at": obj.created_at,
                "total": obj.total,
                "answer": {
                    "created_at": obj.answer.created_at,
                    "choice": obj.answer.choice,
                    "question_name": obj.answer.question.name,
                },
            }
        )

    async def fetch(
        self, clause: QueryExpression
    ):
        result = await self.context.acquire_session().find(PointModel, clause)

        return [self.to_dto(obj) for obj in result]

    async def create(self, payload: schemas.Point) -> None:
        await self.context.acquire_session().save(PointModel(**payload.model_dump()))

    async def get(self, clause: QueryExpression) -> schemas.PointPayload:
        result = self.context.acquire_session().find_one(PointModel, clause)

        if first := result:
            return self.to_dto(first)
        raise "NOT FOUND ERROR"  # TODO add default exception
