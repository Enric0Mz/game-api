from src.database.connection import DbConnectionHandler


class Repository:
    __abstract__ = True

    def __init__(self, context: DbConnectionHandler) -> None:
        self.context = context
        self.context.connect_to_db()
        self.context.transaction_begin()
