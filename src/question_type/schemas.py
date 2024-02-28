from enum import Enum

from src.api.schema import Schema


class Difficulty(Enum):
    VERY_EASY = "very_easy"
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    VERY_HARD = "very_hard"


class QuestyonType(Schema):
    difficulty: Difficulty
    point_multiplier: int
