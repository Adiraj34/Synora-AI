from pydantic import BaseModel


class HabitCreate(BaseModel):
    name: str