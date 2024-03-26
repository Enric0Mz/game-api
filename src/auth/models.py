from datetime import datetime

from odmantic import Field, Model, ObjectId


class TokenModel(Model):
    user_id: ObjectId = Field(unique=True, index=True)
    access_token: str = Field(unique=True)
    refresh_token: str = Field(unique=True)
    created_at: datetime


class UserModel(Model): # User Model here to avoid circular import in user module
    nickname: str = Field(unique=True)
    email: str = Field(unique=True)
    password: str
