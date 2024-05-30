from typing import List


class Task:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description


class TaskManager:
    def __init__(self):
        tasks = List[]
        raise NotImplementedError("to be implemented")

    def add_task(self, title: str, description: str) -> None:
        raise NotImplementedError("to be implemented")

    @property
    def tasks(self) -> List[Task]:
        raise NotImplementedError("to be implemented")

if name == '__main__':
    task_manager = TaskManager()

    task_manager.add_task("Задача 1", "Описание задачи 1")
    task_manager.add_task("Задача 2", "Описание задачи 2")

    tasks = task_manager.tasks
    for idx, task in enumerate(tasks, start=1):
        print(f"Задача {idx}: {task.title} - {task.description}")


