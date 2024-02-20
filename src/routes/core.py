from fastapi import APIRouter

from . import administrative


router = APIRouter(prefix="/api")


@router.get("/health-check")
def health():
    return {"status": "ok"}


router.include_router(administrative.router, prefix="/administrative", tags=["Administrative"])
