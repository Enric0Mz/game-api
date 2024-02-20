from datetime import datetime

from .schema import Schema


class Game(Schema):
    subject: str
    created_at: datetime
    start_at: datetime
    finish_at: datetime
