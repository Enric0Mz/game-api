from datetime import datetime
from odmantic import ObjectId

from src.api.schema import Schema


class Game(Schema):
    id_: ObjectId
    subject: str
    start_at: datetime
    finish_at: datetime


class CreateGame(Game):
    created_at: datetime
