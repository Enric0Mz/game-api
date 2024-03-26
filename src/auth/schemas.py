from datetime import datetime

from odmantic import ObjectId

from src.api.schema import Schema


class Token(Schema):
    user_id: ObjectId
    access_token: str
    refresh_token: str
    created_at: datetime