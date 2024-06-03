from typing import List


class Task:
    def __init__(self, title: str, description: str) -> None:
        self.__title = title
        self.__description = description

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description


class TaskManager(object):
    def __init__(self):
        self.__tasks = []

    def add_task(self, title: str, description: str) -> None:
        self.__tasks.append(Task(title, description))

    @property
    def tasks(self) -> List[Task]:
        return self.__tasks


if __name__ == '__main__':
    task_manager = TaskManager()

    task_manager.add_task("Задача 1", "Описание задачи 1")
    task_manager.add_task("Задача 2", "Описание задачи 2")

    tasks = task_manager.tasks
    for idx, task in enumerate(tasks, start=1):
        print(f"Задача {idx}: {task.title} - {task.description}")


