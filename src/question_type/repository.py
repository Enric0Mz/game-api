from odmantic.query import QueryExpression

from src.database.repository import Repository

from .models import QuestyonTypeModel 
from . import schemas


class QuestionTypeRepository(Repository):
    def to_dto(self, obj: QuestyonTypeModel) -> schemas.QuestyonType:
        return schemas.QuestyonType.model_validate(
            {
                "id": obj.id,
                "difficulty": obj.difficulty,
                "point_multiplier": obj.point_multiplier
            }
        )
    
    async def get(self, clause: QueryExpression):
        result = self.context.acquire_session().find_one(QuestyonTypeModel, clause)
        if first := result:
            return self.to_dto(result)
        raise "NOT FOUND ERROR" #Add proper error handler

    async def create(self, payload: schemas.QuestyonType):
        result = self.context.acquire_session().save(QuestyonTypeModel(**payload.model_dump_json()))
        return self.to_dto(result)

    async def fetch(self, clause: QueryExpression):
        result = self.context.acquire_session().find(QuestyonTypeModel, clause)
        return [self.to_dto(obj) for obj in result]
