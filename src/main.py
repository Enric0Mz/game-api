from fastapi import FastAPI

from src.routes.core import router
from src.api.events import lifespan


def get_application() -> FastAPI:
    _app = FastAPI(title="Game Api", version="0.1.0", debug=True, lifespan=lifespan)
    _app.include_router(router)

    return _app


app = get_application()