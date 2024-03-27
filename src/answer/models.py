from datetime import datetime

from odmantic import EmbeddedModel, Index, Model, ObjectId

from src.question.models import ChoiceModel, QuestyonTypeModelEmbedded


class ChoiceModelEmbedded(EmbeddedModel):
    name: str
    correct: bool
    position: int


class QuestionModelEmbedded(EmbeddedModel):
    name: str
    question_type: QuestyonTypeModelEmbedded
    choices: list[ChoiceModel]
    point_value: int


class AnswerModel(Model):
    user_id: ObjectId
    created_at: datetime
    choice: ChoiceModelEmbedded
    question: QuestionModelEmbedded
