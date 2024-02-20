from datetime import datetime

from odmantic import Model


class GameModel(Model):
    subject: str
    created_at: datetime
    start_at: datetime
    finish_at: datetime
