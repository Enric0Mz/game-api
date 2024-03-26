from datetime import datetime

from odmantic import Model
from odmantic import ObjectId
from odmantic import Field


class TokenModel(Model):
    user_id: ObjectId = Field(unique=True, index=True)
    token: str = Field(unique=True)
    refresh_token: str = Field(unique=True)
    created_at: datetime

