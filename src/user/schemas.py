from odmantic import ObjectId
from pydantic import EmailStr

from src.api.schema import Schema


class User(Schema):
    id: ObjectId
    nickname: str
    email: EmailStr
    password: str
