from fastapi import FastAPI
from app.db.database import engine, Base

import app.models

app = FastAPI(
    title="Project Management API",
    description="API for managing projects and tasks",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "API running"}