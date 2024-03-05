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


class GameQuestionEmbedded(EmbeddedModel):
    id: ObjectId
    question: str
    question_type: QuestyonTypeModel
    swift_channel: str
    choices: list[ChoiceModel]



class Answer(Model):
    user_id: int
    name: str
    created_at: datetime
    choice: ChoiceModelEmbedded
    question: GameQuestionEmbedded

    class Config:
        @staticmethod
        def indexes():
            yield Index(Answer.user_id)
