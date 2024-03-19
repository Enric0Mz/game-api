from datetime import datetime

from src.api.schema import Schema
from src.question.schemas import Choice, Question


class Answer(Schema):
    created_at: datetime
    choice: Choice
    question: Question
