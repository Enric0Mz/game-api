from enum import Enum
from odmantic import ObjectId

from src.api.schema import Schema
from src.game.schemas import ExtendedGame
from src.question_type.schemas import Difficulty
from src.question_type.schemas import QuestionType


class Choice(Schema):
    name: str
    correct: bool
    position: int


class ExtendedChoice(Choice):
    id_: ObjectId | None = None # None included for creation use case


class Question(Schema):
    id_: ObjectId | None = None # None included for creation use case
    name: str
    choices: list[ExtendedChoice]
    question_type: QuestionType
    point_value: int


class ExtendedQuestion(Question):
    game: ExtendedGame


class QuestionPayload(Schema):
    name: str
    choices: list[Choice]
    question_type: Difficulty
    point_value: int
