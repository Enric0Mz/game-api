from datetime import datetime

from odmantic import ObjectId

from src.api.schema import Schema


class Token(Schema):
    user_id: ObjectId
    access_token: str
    refresh_token: str
    created_at: datetime


class ExtendedToken(Token):
    id: ObjectId


class TokenPayload(Schema):
    refresh_token: str


class TokenResponse(Schema):
    access_token: str
    expires: datetime
    refresh_token: str
    type: str
