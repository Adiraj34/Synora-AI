from app.models.habit import Habit


def create_habit(db, habit):

    new_habit = Habit(
        name=habit.name
    )

    db.add(new_habit)
    db.commit()
    db.refresh(new_habit)

    return new_habit


def get_habits(db):
    return db.query(Habit).all()