from src.api.schema import Schema


class UserPayload(Schema):
    nickname: str
    email: str


class CurrentPassword(Schema):
    password: str


class UpdateUserPayload(Schema):
    current: CurrentPassword
    nickname: str | None = None
    password: str | None = None
    confirm_password: str | None = None


class UpdateUser(Schema):
    nickname: str | None = None
    password: str | None = None
