from pydantic import EmailStr
from odmantic import ObjectId

from src.api.schema import Schema


class User(Schema):
    id: ObjectId
    nickname: str
    email: EmailStr
    password: str
