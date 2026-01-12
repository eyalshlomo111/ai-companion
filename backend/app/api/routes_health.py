from fastapi import APIRouter
from app.db import test_db_connection

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/db-health")
def db_health():
    try:
        test_db_connection()
        return {"db": "ok"}
    except Exception as e:
        return {"db": "error", "detail": str(e)}
