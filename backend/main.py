from fastapi import FastAPI
from db import test_db_connection

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-health")
def db_health():
    try:
        test_db_connection()
        return {"db": "ok"}
    except Exception as e:
        return {"db": "error", "detail": str(e)}
