from odmantic import query
from odmantic.query import QueryExpression
from odmantic.exceptions import DuplicateKeyError
from odmantic.query import QueryExpression

from src.database.repository import Repository
from src.api import exc
from src.common.user import User, ExtendedUser

from . import schemas
from .models import TokenModel
from .models import UserModel


class AuthRepository(Repository):
    def to_dto(self, obj: TokenModel) -> schemas.ExtendedToken:
        return schemas.ExtendedToken.model_validate(
            {
                "id": obj.id,
                "user_id": obj.user_id,
                "access_token": obj.access_token,
                "refresh_token": obj.refresh_token,
                "created_at": obj.created_at,
            }
        )

    async def get(self, clause: QueryExpression) -> None:
        result = await self.context.acquire_session().find_one(TokenModel, clause)
        if first := result:
            return self.to_dto(first)

    async def update(self, payload: schemas.Token) -> None:
        if result := await self.get(query.eq(TokenModel.user_id, payload.user_id)):
            return await self.context.acquire_session().save(
                TokenModel(id=result.id, **payload.model_dump())
            )
        else:
            return await self.context.acquire_session().save(
                TokenModel(**payload.model_dump())
            )

    async def delete(self, clause: QueryExpression) -> None:
        result = await self.context.acquire_session().find_one(TokenModel, clause)

        if first := result:
            await self.context.acquire_session().delete(first)


class UserRepository(Repository): # User Repository here to avoid circular import in user module
    def to_dto(self, obj: UserModel) -> User:
        return ExtendedUser.model_validate(
            {
                "id": obj.id,
                "nickname": obj.nickname,
                "email": obj.email,
                "password": obj.password,
            }
        )

    async def create(self, payload: User) -> None:
        try:
            await self.context.acquire_session().save(UserModel(**payload.model_dump()))
        except DuplicateKeyError as e:
            raise exc.already_exists_exception(e, payload)

    async def get(self, clause: QueryExpression) -> User:
        result = await self.context.acquire_session().find_one(UserModel, clause)

        if first := result:
            return self.to_dto(first)
