from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router

import app.models

app = FastAPI(
    title="Project Management API",
    description="API for managing projects and tasks",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
def health_check():
    return {"status": "API running"}