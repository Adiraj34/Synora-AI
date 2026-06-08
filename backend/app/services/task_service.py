tasks = []


def create_task(task):
    tasks.append(task)
    return task


def get_tasks():
    return tasks


def delete_task(task_id):
    if task_id >= len(tasks):
        return None

    return tasks.pop(task_id)


def update_task(task_id, task):
    if task_id >= len(tasks):
        return None

    tasks[task_id] = task
    return task