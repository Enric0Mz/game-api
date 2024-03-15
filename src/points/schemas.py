from datetime import datetime

from src.api.schema import Schema

from src.answer.schemas import Answer
from src.question.schemas import Choice


class SimpleAnswer(Schema):
    created_at: datetime
    choice: Choice
    question_name: str


class Point(Schema):
    created_at: datetime
    total: int
    answer: Answer


class PointPayload(Schema):
    created_at: datetime
    total: int
    answer: SimpleAnswer


class PointsTotal(Schema):
    points: list[PointPayload]
