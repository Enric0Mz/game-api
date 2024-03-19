from src.api.schema import Schema
from pydantic import EmailStr


class User(Schema):
    nickname: str
    email: EmailStr
    password: str
