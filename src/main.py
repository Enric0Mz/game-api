from fastapi import FastAPI


def get_application() -> FastAPI:
    _app = FastAPI(title="Game Api", version="0.1.0", debug=True)

    return _app


app = get_application()