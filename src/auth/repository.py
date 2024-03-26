from odmantic.query import QueryExpression
from odmantic import query

from src.database.repository import Repository

from . import schemas
from .models import TokenModel


class AuthRepository(Repository):
    def to_dto(self, obj: TokenModel) -> schemas.ExtendedToken:
        return schemas.ExtendedToken.model_validate(
            {
                "id": obj.id,
                "user_id": obj.user_id,
                "access_token": obj.access_token,
                "refresh_token": obj.refresh_token,
                "created_at": obj.created_at
            } 
        )


    async def update(self, payload: schemas.Token) -> None:
        if result := await self.get(query.eq(TokenModel.user_id, payload.user_id)):
            return await self.context.acquire_session().save(TokenModel(id=result.id, **payload.model_dump()))
        else:
            return await self.context.acquire_session().save(TokenModel(**payload.model_dump()))
    
    async def get(self, clause: QueryExpression) -> None:
        result = await self.context.acquire_session().find_one(TokenModel, clause)

        if first := result:
            return self.to_dto(first)