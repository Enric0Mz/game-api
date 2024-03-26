from odmantic.exceptions import DuplicateKeyError
from odmantic.query import QueryExpression

from src.api import exc
from src.database.repository import Repository

from . import schemas
from .models import UserModel


class UserRepository(Repository):
    def to_dto(self, obj: UserModel) -> schemas.User:
        return schemas.ExtendedUser.model_validate(
            {
                "id": obj.id,
                "nickname": obj.nickname,
                "email": obj.email,
                "password": obj.password,
            }
        )

    async def create(self, payload: schemas.User) -> None:
        try:
            await self.context.acquire_session().save(UserModel(**payload.model_dump()))
        except DuplicateKeyError as e:
            raise exc.already_exists_exception(e, payload)

    async def get(self, clause: QueryExpression) -> schemas.User:
        result = await self.context.acquire_session().find_one(UserModel, clause)

        if first := result:
            return self.to_dto(first)
