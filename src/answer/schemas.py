from datetime import datetime

from src.api.schema import Schema
from src.question.schemas import Choice
from src.question.schemas import Question


class Answer(Schema):
    user_id: int
    created_at: datetime
    choice: Choice
    question: Question
