from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.database import Base


class LearningSession(Base):
    __tablename__ = "learning_sessions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    subject = Column(String)

    duration = Column(Integer)