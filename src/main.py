from fastapi import FastAPI

from src.api.events import lifespan

from .routes import router


def get_application() -> FastAPI:
    _app = FastAPI(title="Game Api", version="0.1.0", debug=True, lifespan=lifespan)
    _app.include_router(router)

    return _app


app = get_application()
