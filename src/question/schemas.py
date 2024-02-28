from enum import Enum

from src.api.schema import Schema
from src.game.schemas import Game
from src.question_type.schemas import Difficulty
from src.question_type.schemas import QuestyonType

class Choice(Schema):
    name: str
    correct: bool
    position: int


class Question(Schema):
    name: str
    choices: list[Choice]
    question_type: QuestyonType
    point_value: int


class ExtendedQuestion(Schema):
    game: Game