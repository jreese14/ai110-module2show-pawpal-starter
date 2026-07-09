from pawpal_system import Owner, Pet, Task, Schedule


def main():
    owner = Owner(name="Alice", available_time=120, pets=[])

    dog = Pet(name="Buddy", species="Dog", age=3, owner=owner)
    cat = Pet(name="Whiskers", species="Cat", age=2, owner=owner)

    owner.add_pet(dog)
    owner.add_pet(cat)

    task1 = Task(
        task_name="Feed Buddy",
        duration=10,
        priority="high",
        frequency="daily",
        completed=False,
        owner=owner,
        pet=dog
    )

    task2 = Task(
        task_name="Play with Buddy",
        duration=30,
        priority="medium",
        frequency="daily",
        completed=False,
        owner=owner,
        pet=dog
    )

    task3 = Task(
        task_name="Clean Whiskers' litter box",
        duration=15,
        priority="low",
        frequency="daily",
        completed=False,
        owner=owner,
        pet=cat
    )

    task4 = Task(
        task_name="Groom Whiskers",
        duration=25,
        priority="high",
        frequency="weekly",
        completed=True,
        owner=owner,
        pet=cat
    )

    schedule = Schedule(owner=owner, tasks=[])
    schedule.add_task(task1)
    schedule.add_task(task2)
    schedule.add_task(task3)
    schedule.add_task(task4)

    print("\n" + "="*50)
    print("Today's Schedule")
    print("="*50)
    schedule.display_schedule()


if __name__ == "__main__":
    main()
