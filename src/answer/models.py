from datetime import datetime

from odmantic import Model
from odmantic import EmbeddedModel
from odmantic import Index
from odmantic import ObjectId

from src.question.models import ChoiceModel, QuestyonTypeModelEmbedded


class ChoiceModelEmbedded(EmbeddedModel):
    name: str
    correct: bool
    position: int


class QuestionModelEmbedded(EmbeddedModel):
    id: ObjectId
    question: str
    question_type: QuestyonTypeModelEmbedded
    choices: list[ChoiceModel]



class AnswerModel(Model): #TODO add user later
    created_at: datetime
    choice: ChoiceModelEmbedded
    question: QuestionModelEmbedded
