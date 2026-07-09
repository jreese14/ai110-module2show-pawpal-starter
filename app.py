import streamlit as st
from pawpal_system import Owner, Pet, Task, Schedule

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = None

if "schedule" not in st.session_state:
    st.session_state.schedule = None

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
col1, col2 = st.columns(2)
with col1:
    owner_name = st.text_input("Owner name", value="Jordan")
with col2:
    available_time = st.number_input("Available time (minutes)", min_value=10, max_value=1440, value=120)

if st.button("Create Owner"):
    st.session_state.owner = Owner(name=owner_name, available_time=available_time, pets=[])
    st.session_state.tasks = []
    st.success(f"Owner '{owner_name}' created!")
    st.rerun()

if st.session_state.owner:
    st.write(f"**Current Owner:** {st.session_state.owner.name}")

    pet_name = st.text_input("Pet name", value="Mochi")
    species = st.selectbox("Species", ["dog", "cat", "other"])

    if st.button("Add Pet"):
        pet = Pet(name=pet_name, species=species, age=1, owner=st.session_state.owner)
        st.session_state.owner.add_pet(pet)
        st.success(f"Pet '{pet_name}' added!")

    if st.session_state.owner.pets:
        st.write(f"**Pets:** {[pet.name for pet in st.session_state.owner.pets]}")

    st.markdown("### Tasks")
    st.caption("Add tasks for your pet(s).")

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    if st.session_state.owner and st.session_state.owner.pets:
        col1, col2, col3 = st.columns(3)
        with col1:
            task_title = st.text_input("Task title", value="Morning walk")
        with col2:
            duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
        with col3:
            priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

        col1, col2 = st.columns(2)
        with col1:
            frequency = st.selectbox("Frequency", ["daily", "weekly", "once"], index=0)
        with col2:
            selected_pet = st.selectbox("Pet", [pet.name for pet in st.session_state.owner.pets])

        if st.button("Add task", use_container_width=True):
            pet = next(p for p in st.session_state.owner.pets if p.name == selected_pet)
            task = Task(
                task_name=task_title,
                duration=int(duration),
                priority=priority,
                frequency=frequency,
                completed=False,
                owner=st.session_state.owner,
                pet=pet
            )
            st.session_state.tasks.append(task)
            st.success(f"Task '{task_title}' added to {selected_pet}!")

        if st.session_state.tasks:
            st.write("Current tasks:")
            for i, task in enumerate(st.session_state.tasks):
                col1, col2, col3 = st.columns([0.5, 3, 0.5])
                with col1:
                    is_done = st.checkbox("Done", value=task.completed, key=f"task_{i}")
                    if is_done != task.completed:
                        task.completed = is_done
                with col2:
                    status = "✓" if task.completed else "○"
                    st.write(f"{status} {task.task_name} ({task.duration}min, Priority: {task.priority}, Freq: {task.frequency}) - {task.pet.name}")
                with col3:
                    if st.button("Remove", key=f"remove_{i}"):
                        st.session_state.tasks.pop(i)
                        st.rerun()
        else:
            st.info("No tasks yet. Add one above.")
    else:
        st.info("Add a pet first.")

st.divider()

st.subheader("Build Schedule")
st.caption("Generate an optimized schedule based on task priorities.")

if st.button("Generate schedule"):
    if st.session_state.owner and st.session_state.tasks:
        st.session_state.schedule = Schedule(owner=st.session_state.owner, tasks=st.session_state.tasks)
        st.success("Schedule generated!")
        schedule_text = st.session_state.schedule.get_schedule_text()

        total_time = sum(task.duration for task in st.session_state.tasks)
        if total_time > st.session_state.owner.available_time:
            st.warning(f"⚠️ Tasks exceed available time! ({total_time} min scheduled vs {st.session_state.owner.available_time} min available)")

        st.code(schedule_text, language="")
    else:
        st.warning("Please create an owner and add at least one task first.")
