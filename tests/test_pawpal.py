import unittest
from pawpal_system import Owner, Pet, Task, Schedule


class TestTaskCompletion(unittest.TestCase):
    """Test that mark_complete() changes task status."""

    def setUp(self):
        self.owner = Owner(name="Alice", available_time=120, pets=[])
        self.pet = Pet(name="Buddy", species="Dog", age=3, owner=self.owner)

    def test_mark_complete(self):
        task = Task(
            task_name="Feed Buddy",
            duration=10,
            priority="high",
            frequency="daily",
            completed=False,
            owner=self.owner,
            pet=self.pet
        )
        self.assertFalse(task.completed)
        task.mark_complete()
        self.assertTrue(task.completed)


class TestTaskAddition(unittest.TestCase):
    """Test that adding a task to a schedule for a pet works correctly."""

    def setUp(self):
        self.owner = Owner(name="Alice", available_time=120, pets=[])
        self.pet = Pet(name="Buddy", species="Dog", age=3, owner=self.owner)
        self.owner.add_pet(self.pet)
        self.schedule = Schedule(owner=self.owner, tasks=[])

    def test_add_task_to_schedule(self):
        task = Task(
            task_name="Feed Buddy",
            duration=10,
            priority="high",
            frequency="daily",
            completed=False,
            owner=self.owner,
            pet=self.pet
        )
        self.assertEqual(len(self.schedule.tasks), 0)
        self.schedule.add_task(task)
        self.assertEqual(len(self.schedule.tasks), 1)

    def test_pet_task_retrieval(self):
        """Verify tasks for a specific pet can be retrieved from schedule."""
        task1 = Task(
            task_name="Feed Buddy",
            duration=10,
            priority="high",
            frequency="daily",
            completed=False,
            owner=self.owner,
            pet=self.pet
        )
        task2 = Task(
            task_name="Play with Buddy",
            duration=30,
            priority="medium",
            frequency="daily",
            completed=False,
            owner=self.owner,
            pet=self.pet
        )
        self.schedule.add_task(task1)
        self.schedule.add_task(task2)

        pet_tasks = [t for t in self.schedule.tasks if t.pet == self.pet]
        self.assertEqual(len(pet_tasks), 2)


if __name__ == "__main__":
    unittest.main()
