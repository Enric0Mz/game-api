from src.api.schema import Schema
from src.game.schemas import Game


class Choice(Schema):
    name: str
    correct: bool
    position: int


class QuestyonType(Schema):
    difficulty: str
    point_multiplier: int


class Question(Schema):
    name: str
    choices: list[Choice]
    question_type: QuestyonType
    game: Game
    point_value: int
