from odmantic.exceptions import DuplicateKeyError
from odmantic.query import QueryExpression

from src.api import exc
from src.database.repository import Repository
from src.common.user import User, ExtendedUser

from . import schemas
from .models import UserModel


class UserRepository(Repository):
    def to_dto(self, obj: UserModel) -> User:
        return ExtendedUser.model_validate(
            {
                "id": obj.id,
                "nickname": obj.nickname,
                "email": obj.email,
                "password": obj.password,
            }
        )

    async def get(self, clause: QueryExpression) -> ExtendedUser:
        result = await self.context.acquire_session().find_one(UserModel, clause)

        if first := result:
            return self.to_dto(first)
        
    async def update(self, payload: schemas.UpdateUser) -> None:
        await self.context.acquire_session().save(UserModel(**payload.model_dump(exclude_unset=True)))
