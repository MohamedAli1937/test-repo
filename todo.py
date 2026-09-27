def add_task(tasks, task):
    if task.strip() == "":
        return tasks
    tasks.append(task)
    return tasks
    
def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
    return tasks

def count_pending(tasks):
    return len([task for task in tasks if not task.startswith("[x]")])
