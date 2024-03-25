from odmantic.query import QueryExpression
from odmantic.exceptions import DuplicateKeyError

from src.api import exc
from src.database.repository import Repository

from .models import UserModel
from . import schemas


class UserRepository(Repository):
    def to_dto(self, obj: UserModel) -> schemas.User:
        return schemas.User.model_validate(
            {
                "id": obj.id,
                "nickname": obj.nickname,
                "email": obj.email,
            }
        )
    
    async def create(self, payload: schemas.User) -> None:
        try:
            await self.context.acquire_session().save(UserModel(**payload.model_dump()))
        except DuplicateKeyError as e:
            raise exc.already_exists_exception(e, payload)

    async def get(self, clause: QueryExpression) -> schemas.User:
        result = self.context.acquire_session().find_one(UserModel, clause)

        if first := result:
            return self.to_dto(first)
