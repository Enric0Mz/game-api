from enum import Enum

from src.api.schema import Schema
from src.game.schemas import Game


class Difficulty(Enum):
    VERY_EASY = "very_easy"
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    VERY_HARD = "very_hard"


class Choice(Schema):
    name: str
    correct: bool
    position: int


class QuestyonType(Schema):
    difficulty: Difficulty
    point_multiplier: int


class Question(Schema):
    name: str
    choices: list[Choice]
    question_type: QuestyonType
    point_value: int


class ExtendedQuestion(Schema):
    game: Game