from datetime import datetime

from odmantic import Model, EmbeddedModel

from src.answer.models import ChoiceModelEmbedded, QuestionModelEmbedded


class AnswerModelEmbedded(EmbeddedModel):  # TODO add user later
    created_at: datetime
    choice: ChoiceModelEmbedded
    question: QuestionModelEmbedded


class Point(Model): # TODO add user later
    created_at: datetime
    total: int
    answer: AnswerModelEmbedded


class PointsTotal(Model):
    points: list[Point]
