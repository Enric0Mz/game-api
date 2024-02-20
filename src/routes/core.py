from fastapi import APIRouter


router = APIRouter(prefix="/api")


@router.get("/health-check")
def health():
    return {"status": "ok"}
