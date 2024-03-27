from src.api.schema import Schema


class UserPayload(Schema):
    nickname: str
    email: str


class CurrentPassword(Schema):
    password: str


class UpdateUserPayload(Schema):
    current: CurrentPassword
    nickname: str | None
    password: str | None
    confirm_password: str | None 


class UpdateUser(Schema):
    nickname: str | None
    password: str | None
