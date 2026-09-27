from todo import add_task, remove_task, count_pending


def test_add_task():
    tasks = []
    add_task(tasks, "Learn Python")
    assert tasks == ["Learn Python"]


def test_remove_task():
    tasks = ["Learn Python", "Build AI"]
    remove_task(tasks, "Learn Python")
    assert tasks == ["Build AI"]


def test_count_pending():
    tasks = ["Learn Python", "[x] Build AI", "Study"]
    assert count_pending(tasks) == 2
