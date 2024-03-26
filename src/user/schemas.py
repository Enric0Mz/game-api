from odmantic import ObjectId
from pydantic import EmailStr

from src.api.schema import Schema


class User(Schema):
    nickname: str
    email: EmailStr
    password: str


class ExtendedUser(User):
    id: ObjectId