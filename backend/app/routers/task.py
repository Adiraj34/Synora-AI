from fastapi import APIRouter
from app.schemas.task import TaskCreate
from app.services.task_service import (
    create_task,
    get_tasks,
    delete_task,
    update_task,
)

router = APIRouter()


@router.post("/tasks")
def add_task(task: TaskCreate):
    return create_task(task)


@router.get("/tasks")
def view_tasks():
    return get_tasks()


@router.delete("/tasks/{task_id}")
def remove_task(task_id: int):

    task = delete_task(task_id)

    if task is None:
        return {"error": "Task not found"}

    return task


@router.put("/tasks/{task_id}")
def edit_task(task_id: int, task: TaskCreate):

    updated = update_task(task_id, task)

    if updated is None:
        return {"error": "Task not found"}

    return updated