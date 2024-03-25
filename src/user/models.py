from odmantic import Model, Field


class UserModel(Model):
    nickname: str = Field(unique=True)
    email: str = Field(unique=True)
    password: str
