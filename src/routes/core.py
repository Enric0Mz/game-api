from fastapi import APIRouter

from . import administrative
from . import microservice



router = APIRouter(prefix="/api")


@router.get("/health-check")
def health():
    return {"status": "ok"}


router.include_router(administrative.router, prefix="/administrative", tags=["Administrative"])
router.include_router(microservice.router, prefix="/microservice", tags=["Microservice"])
