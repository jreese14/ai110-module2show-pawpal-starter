from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    task_name: str
    duration: int
    priority: int
    completed: bool

    def mark_complete(self):
        pass

    def edit_task(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int

    def update_info(self):
        pass

    def display_info(self):
        pass


@dataclass
class Owner:
    name: str
    available_time: int

    def update_info(self):
        pass

    def set_available_time(self, time: int):
        pass


@dataclass
class Schedule:
    tasks: List[Task]
    total_time: int

    def add_task(self, task: Task):
        pass

    def generate_schedule(self):
        pass

    def display_schedule(self):
        pass
