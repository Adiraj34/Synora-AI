from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.database import Base


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    task_name = Column(String)

    start_time = Column(String)

    end_time = Column(String)