from odmantic.query import QueryExpression

from src.database.repository import Repository

from . import schemas
from .models import TokenModel


class AuthRepository(Repository):
    def to_dto(self, obj: TokenModel) -> schemas.Token:
        return schemas.Token.model_validate(
            {
                "user_id": obj.user_id,
                "access_token": obj.access_token,
                "refresh_token": obj.refresh_token,
                "created_at": obj.created_at
            } 
        )


    async def update(self, payload: schemas.Token) -> None:
        return await self.context.acquire_session().save(TokenModel(**payload.model_dump()))
