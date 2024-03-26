from datetime import datetime

from odmantic import Field, Model, ObjectId


class TokenModel(Model):
    user_id: ObjectId = Field(unique=True, index=True)
    access_token: str = Field(unique=True)
    refresh_token: str = Field(unique=True)
    created_at: datetime
