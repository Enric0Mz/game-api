from src.api.schema import Schema


class UserPayload(Schema):
    nickname: str
    email: str