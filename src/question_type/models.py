from odmantic import Model


class QuestyonTypeModel(Model):
    difficulty: str
    point_multiplier: int
