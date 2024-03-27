from datetime import datetime
from odmantic import ObjectId

from odmantic import EmbeddedModel, Model

from src.answer.models import ChoiceModelEmbedded, QuestionModelEmbedded


class AnswerModelEmbedded(EmbeddedModel):
    user_id: ObjectId 
    created_at: datetime
    choice: ChoiceModelEmbedded
    question: QuestionModelEmbedded


class PointModel(Model):
    created_at: datetime
    total: int
    answer: AnswerModelEmbedded
