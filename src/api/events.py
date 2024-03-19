import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.config import database_config, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        app.on_event("startup")
        engine.connect_to_db()
        await database_config()
        yield
    except asyncio.exceptions.CancelledError:
        pass
    finally:
        app.on_event("shutdown")
        engine.connection_close()
