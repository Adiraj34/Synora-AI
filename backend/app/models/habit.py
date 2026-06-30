from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.database import Base


class Habit(Base):
    __tablename__ = "habits"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    streak = Column(
        Integer,
        default=0
    )

    completed = Column(
        String,
        default="No"
    )