from fastapi import FastAPI
from app.routers.task import router as task_router

app = FastAPI(
    title="Synora AI",
    description="AI Powered Productivity Copilot",
    version="0.1.0",
)

app.include_router(task_router)


@app.get("/")
def root():
    return {
        "project": "Synora AI",
        "status": "running",
        "version": "0.1.0",
    }