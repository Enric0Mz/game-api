from enum import Enum

from src.api.schema import Schema


class Difficulty(str, Enum):
    VERY_EASY = "very_easy"
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    VERY_HARD = "very_hard"


POINT_MULTIPLIERS = {
    Difficulty.VERY_EASY: 1,
    Difficulty.EASY: 2,
    Difficulty.MEDIUM: 3,
    Difficulty.HARD: 4,
    Difficulty.VERY_HARD: 5,
}


class QuestionType(Schema):
    name: Difficulty
    point_multiplier: int
