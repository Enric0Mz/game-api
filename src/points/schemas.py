from datetime import datetime

from src.api.schema import Schema

from src.answer.schemas import Answer


class Point(Schema):
    created_at: datetime
    total: int
    answer: Answer


class PointsTotal(Schema):
    points: list[Point]
