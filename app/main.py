from fastapi import FastAPI

app = FastAPI(
    title="Gestión de Proyectos API",
    description="API para gestionar proyectos, tareas y usuarios.",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "API is running!"}
