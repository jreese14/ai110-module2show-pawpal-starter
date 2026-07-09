from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    task_name: str
    duration: int
    priority: str
    frequency: str
    completed: bool
    owner: Owner
    pet: Pet
    scheduled_time: str = None

    VALID_PRIORITIES = {"high", "medium", "low"}
    PRIORITY_ORDER = {"high": 1, "medium": 2, "low": 3}

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def edit_task(self, task_name: str = None, duration: int = None, priority: str = None, frequency: str = None):
        """Edit task details: name, duration, priority, and/or frequency."""
        if task_name is not None:
            self.task_name = task_name
        if duration is not None:
            if duration <= 0:
                raise ValueError("Duration must be positive")
            self.duration = duration
        if priority is not None:
            if priority.lower() not in self.VALID_PRIORITIES:
                raise ValueError(f"Priority must be one of: {', '.join(self.VALID_PRIORITIES)}")
            self.priority = priority.lower()
        if frequency is not None:
            self.frequency = frequency


@dataclass
class Pet:
    name: str
    species: str
    age: int
    owner: Owner

    def update_info(self, name: str = None, species: str = None, age: int = None):
        """Update pet's name, species, and/or age."""
        if name is not None:
            self.name = name
        if species is not None:
            self.species = species
        if age is not None:
            if age < 0:
                raise ValueError("Age cannot be negative")
            self.age = age

    def display_info(self):
        """Display pet's information."""
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Owner: {self.owner.name}")


@dataclass
class Owner:
    name: str
    available_time: int
    pets: List[Pet]

    def update_info(self, name: str = None, available_time: int = None):
        """Update owner's name and/or available time."""
        if name is not None:
            self.name = name
        if available_time is not None:
            self.available_time = available_time

    def set_available_time(self, time: int):
        """Set the owner's available time."""
        if time < 0:
            raise ValueError("Available time cannot be negative")
        self.available_time = time

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list of pets."""
        if pet not in self.pets:
            self.pets.append(pet)
            pet.owner = self

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner's list of pets."""
        if pet in self.pets:
            self.pets.remove(pet)


@dataclass
class Schedule:
    owner: Owner
    tasks: List[Task]

    def add_task(self, task: Task) -> None:
        """Add a task to the schedule if it belongs to this owner."""
        if task.owner != self.owner:
            raise ValueError("Task does not belong to this owner")
        if task not in self.tasks:
            self.tasks.append(task)

    def get_all_pet_tasks(self) -> List[Task]:
        """Retrieve all tasks belonging to the owner's pets by iterating through pets."""
        all_tasks = []
        for pet in self.owner.pets:
            for task in self.tasks:
                if task.pet == pet:
                    all_tasks.append(task)
        return all_tasks

    def generate_schedule(self) -> List[Task]:
        """Organize tasks by priority, assign scheduled times, and check feasibility."""
        from datetime import datetime, timedelta

        pet_tasks = self.get_all_pet_tasks()
        sorted_tasks = sorted(pet_tasks, key=lambda t: Task.PRIORITY_ORDER[t.priority])

        total_time = sum(task.duration for task in sorted_tasks)
        if total_time > self.owner.available_time:
            print(f"Warning: Total task duration ({total_time}) exceeds available time ({self.owner.available_time})")

        start_time = datetime.strptime("08:00", "%H:%M")
        for task in sorted_tasks:
            task.scheduled_time = start_time.strftime("%H:%M")
            start_time += timedelta(minutes=task.duration)

        return sorted_tasks

    def get_schedule_text(self) -> str:
        """Return the schedule as formatted text."""
        organized = self.generate_schedule()

        if not organized:
            return f"No tasks scheduled for {self.owner.name}"

        lines = [
            f"=== Schedule for {self.owner.name} ===",
            f"Available time: {self.owner.available_time} minutes",
            ""
        ]

        total_time = 0
        for task in organized:
            status = "✓" if task.completed else "○"
            lines.append(f"{task.scheduled_time} — {status} {task.task_name} (Pet: {task.pet.name}, {task.duration}min) [priority: {task.priority}]")
            total_time += task.duration

        lines.append("")
        lines.append(f"Total scheduled time: {total_time} minutes")

        if total_time > self.owner.available_time:
            lines.append("")
            lines.append(f"⚠️  WARNING: Tasks exceed available time by {total_time - self.owner.available_time} minutes!")

        return "\n".join(lines)

    def display_schedule(self) -> None:
        """Display the schedule sorted by priority with scheduled times."""
        organized = self.generate_schedule()

        if not organized:
            print(f"No tasks scheduled for {self.owner.name}")
            return

        print(f"\n=== Schedule for {self.owner.name} ===")
        print(f"Available time: {self.owner.available_time} minutes\n")

        total_time = 0
        for task in organized:
            status = "✓" if task.completed else "○"
            print(f"{task.scheduled_time} — {status} {task.task_name} (Pet: {task.pet.name}, {task.duration}min) [priority: {task.priority}]")
            total_time += task.duration

        print(f"\nTotal scheduled time: {total_time} minutes")
