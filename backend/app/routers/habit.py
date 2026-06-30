from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.habit import HabitCreate
from app.services.habit_service import (
    create_habit,
    get_habits
)

router = APIRouter()


@router.post("/habits")
def add_habit(
    habit: HabitCreate,
    db: Session = Depends(get_db)
):
    return create_habit(db, habit)


@router.get("/habits")
def view_habits(
    db: Session = Depends(get_db)
):
    return get_habits(db)