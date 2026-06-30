from fastapi import FastAPI
from app.database.database import engine
from app.models.task import Task
from app.routers.task import router as task_router
from app.models.user import User
from app.routers.auth import router as auth_router
from app.models.habit import Habit
from app.models.schedule import Schedule
from app.models.learning_session import LearningSession
from app.routers.habit import router as habit_router

Task.metadata.create_all(bind=engine)
User.metadata.create_all(bind=engine)

Habit.metadata.create_all(bind=engine)
Schedule.metadata.create_all(bind=engine)
LearningSession.metadata.create_all(bind=engine)

app = FastAPI(
    title="Synora AI",
    description="AI Powered Productivity Copilot",
    version="0.2.0",
)

app.include_router(task_router)
app.include_router(auth_router)
app.include_router(habit_router)

@app.get("/")
def root():
    return {
        "project": "Synora AI",
        "status": "running",
        "version": "0.2.0",
    }
