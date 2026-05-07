# In-memory list of tasks for the to-do application.
tasks = []

# Identifier used to assign a unique ID to each new task.
next_task_id = 1


def add_task(task_name):
    """Add a new task with a unique ID and mark it as not done."""
    global next_task_id
    task = {
        'id': next_task_id,
        'name': task_name,
        'done': False,
    }
    tasks.append(task)
    next_task_id += 1
    return f"Task added: {task_name}"


def get_all_tasks():
    """Return a copy of the full task list."""
    return list(tasks)


def get_pending_tasks():
    """Return tasks that have not yet been completed."""
    return [task for task in tasks if not task['done']]


def get_completed_tasks():
    """Return tasks that are marked as done."""
    return [task for task in tasks if task['done']]


def mark_as_done(task_id):
    """Mark the task with the given ID as completed."""
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            return True
    return False


def delete_task(task_id):
    """Remove the task with the specified ID from the list."""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return True


def count_tasks_stats():
    """Return a summary of completed and pending task counts."""
    return {
        'completed': len(get_completed_tasks()),
        'pending': len(get_pending_tasks()),
    }


def clear_completed():
    """Remove all tasks that have been marked as completed."""
    global tasks
    tasks = [task for task in tasks if not task['done']]
    return True
