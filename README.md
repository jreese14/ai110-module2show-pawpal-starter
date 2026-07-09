# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
==================================================
Today's Schedule
==================================================

=== Schedule for Alice ===
Available time: 120 minutes

08:00 — ○ Feed Buddy (Pet: Buddy, 10min) [priority: high]
08:10 — ✓ Groom Whiskers (Pet: Whiskers, 25min) [priority: high]
08:35 — ○ Play with Buddy (Pet: Buddy, 30min) [priority: medium]
09:05 — ○ Clean Whiskers' litter box (Pet: Whiskers, 15min) [priority: low]

Total scheduled time: 80 minutes
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

The scheduler organizes tasks by user-specified time slots and provides filtering, conflict detection, and automatic recurring task management.

| Feature | Method(s) | Description |
|---------|-----------|-------------|
| **Task Sorting** | `Schedule.sort_by_time()` | Sorts tasks chronologically by `scheduled_time`. O(n log n) single-pass algorithm. Tasks without times placed first. |
| **Filtering** | `Schedule.filter_tasks(completed, pet_name)` | Filters tasks by completion status and/or pet name. Single-pass list comprehension with combined boolean conditions. |
| **Conflict Detection** | `Schedule.detect_scheduling_conflicts()` | Detects multiple tasks at the same time slot and returns warning messages (lightweight, non-blocking). Groups tasks by time in O(n) pass. |
| **Recurring Tasks** | `Schedule.complete_task()` | Marks a task complete and auto-creates next occurrence for daily/weekly tasks using `timedelta`. Daily +1 day, weekly +7 days. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
