from lazyfields import is_initialized, lazyfield
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from yarl import URL

from src.core import settings   


class DbConnectionHandler:
    def __init__(self) -> None:
        self._connection_uri = settings.DB_HOST
        url = URL(settings.DB_HOST)
        self._database_name = url.path.removeprefix("/") or settings.DB_NAME

    @lazyfield
    def _client(self):
        return AsyncIOMotorClient(self.get_connection_uri())

    @property
    def _db_connection(self):
        return AIOEngine(client=self._client, database=self._database_name)

    def connect_to_db(self):
        if not is_initialized(self, "_client"):
            self._client

    def get_connection_uri(self):
        return self._connection_uri

    def acquire_session(self):
        return self._db_connection

    def transaction_begin(self):
        return self._db_connection.transaction()

    def connection_close(self):
        if not is_initialized(self, "_client"):
            return
        return self._client.close()
