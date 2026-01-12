from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.deps import get_db

router = APIRouter(tags=["health"])

@router.get("/health")
def health(db: Session = Depends(get_db)):
    # real DB check
    db.execute(text("SELECT 1"))
    return {"status": "ok", "db": "ok"}
