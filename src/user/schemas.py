from src.api.schema import Schema


class UserPayload(Schema):
    nickname: str
    email: str


class CurrentPassword(Schema):
    password: str


class UpdateUserPayload(Schema):
    current: CurrentPassword
    nickname: str
    password: str
    confirm_password: str 


class UpdateUser(Schema):
    nickname: str | None
    password: str | None
