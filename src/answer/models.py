from datetime import datetime

from odmantic import Model
from odmantic import EmbeddedModel
from odmantic import Index
from odmantic import ObjectId

from src.question.models import ChoiceModel
from src.question_type.models import QuestyonTypeModel


class ChoiceModelEmbedded(EmbeddedModel):
    name: str
    correct: bool
    position: int


class QuestionModelEmbedded(EmbeddedModel):
    id: ObjectId
    question: str
    question_type: QuestyonTypeModel
    swift_channel: str
    choices: list[ChoiceModel]



class AnswerModel(Model):
    user_id: int
    name: str
    created_at: datetime
    choice: ChoiceModelEmbedded
    question: QuestionModelEmbedded

    class Config:
        @staticmethod
        def indexes():
            yield Index(AnswerModel.user_id)
