from datetime import datetime
from odmantic import ObjectId

from src.api.schema import Schema


class Game(Schema):
    subject: str
    start_at: datetime
    finish_at: datetime


class CreateGame(Game):
    created_at: datetime


class ExtendedGame(CreateGame):
    id_: ObjectId 


