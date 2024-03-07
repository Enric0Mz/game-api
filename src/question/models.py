from datetime import datetime

from odmantic import ObjectId
from odmantic import Model
from odmantic import EmbeddedModel

from src.question_type.schemas import Difficulty


class ChoiceModel(Model):
    name: str
    correct: bool
    position: int


class QuestyonTypeModelEmbedded(EmbeddedModel):
    name: Difficulty
    point_multiplier: int


class GameModelEmbedded(EmbeddedModel):
    id_: ObjectId
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
