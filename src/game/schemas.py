from datetime import datetime

from src.api.schema import Schema


class Game(Schema):
    subject: str
    start_at: datetime
    finish_at: datetime


class CreateGame(Game):
    created_at: datetime
