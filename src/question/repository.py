from odmantic.query import QueryExpression

from src.database.repository import Repository

from src.question.models import QuestionModel
from src.question import schemas


class QuestionRepository(Repository):
    def to_dto(self, obj: QuestionModel) -> schemas.ExtendedQuestion:
        return schemas.ExtendedQuestion.model_validate(
            {
                "id_": obj.id,
                "name": obj.name,
                "choices": [choice for choice in obj.choices],
                "question_type": obj.question_type,
                "game": obj.game,
                "point_value": obj.point_value
            }
        )
    
    async def fetch(self, clause: QueryExpression):
        result = await self.context.acquire_session().find(QuestionModel, clause)
        return [self.to_dto(obj) for obj in result]
    
    async def get(self, clause: QueryExpression):
        result = await self.context.acquire_session().find_one(QuestionModel, clause)
        if first := result:
            return self.to_dto(first)
        raise "NOT FOUND ERROR" #TODO add default exception

    async def create(self, payload: schemas.ExtendedQuestion):
        print("AQUI")
        await self.context.acquire_session().save(QuestionModel(**payload.model_dump()))
