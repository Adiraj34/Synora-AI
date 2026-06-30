from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate
from app.services.task_service import (
    create_task,
    get_tasks,
    delete_task,
    update_task,
)
from app.database.database import get_db

router = APIRouter()


@router.post("/tasks")
def add_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return create_task(db, task)


@router.get("/tasks")
def view_tasks(
    db: Session = Depends(get_db)
):
    return get_tasks(db)


@router.delete("/tasks/{task_id}")
def remove_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    task = delete_task(db, task_id)

    if task is None:
        return {"error": "Task not found"}

    return task


@router.put("/tasks/{task_id}")
def edit_task(
    task_id: int,
    task: TaskCreate,
    db: Session = Depends(get_db)
):

    updated = update_task(
        db,
        task_id,
        task
    )

    if updated is None:
        return {"error": "Task not found"}

    return updated