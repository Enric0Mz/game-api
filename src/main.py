from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.events import lifespan

from .routes import router


def get_application() -> FastAPI:
    _app = FastAPI(title="Game Api", version="0.1.0", debug=True, lifespan=lifespan)
    _app.include_router(router)
    _app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
