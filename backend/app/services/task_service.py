from app.models.task import Task


def create_task(db, task):

    new_task = Task(
        title=task.title,
        priority=task.priority
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_tasks(db):
    return db.query(Task).all()


def delete_task(db, task_id):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if task is None:
        return None

    db.delete(task)
    db.commit()

    return task


def update_task(db, task_id, task):

    existing_task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if existing_task is None:
        return None

    existing_task.title = task.title
    existing_task.priority = task.priority

    db.commit()
    db.refresh(existing_task)

    return existing_task