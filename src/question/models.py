from datetime import datetime

from odmantic import Model
from odmantic import EmbeddedModel


class ChoiceModel(Model):
    name: str
    correct: bool
    position: int


class QuestyonTypeModelEmbedded(EmbeddedModel):
    difficulty: str
    point_multiplier: int


class GameModelEmbedded(EmbeddedModel):
    subject: str
    created_at: datetime
    start_at: datetime
    finish_at: datetime


class QuestionModel(Model):
    name: str
    choices: list[ChoiceModel]
    question_type: QuestyonTypeModelEmbedded
    game: GameModelEmbedded
    point_value: int
