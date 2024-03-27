from datetime import datetime
from odmantic import ObjectId

from src.api.schema import Schema
from src.question.schemas import Choice, Question


class Answer(Schema):
    user_id: ObjectId
    created_at: datetime
    choice: Choice
    question: Question
