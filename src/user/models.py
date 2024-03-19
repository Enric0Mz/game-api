from odmantic import Model


class UserModel(Model):
    nickname: str
    email: str
    password: str
