# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

Core actions:
1. Add owner + pet information
2. Create and edit pet care tasks
3. Generate and view a daily care schedule

For my initial UML design, I will have four classes: Owner, Pet, Task, and Schedule. The Owner class will store the owner's information, such as their name and available time for pet care. The Pet class will store information about the pet, including its name, species, and age. The Task class will represent individual pet care tasks, such as feeding, walking, or meds, along with each task's duration, priority, and completion status. Finally, the Schedule class will organize tasks, generate a daily schedule based on priorities and time constraints, and display the schedule to the user.

Owner: Attributes: name, available_time; Methods: update_info(), set_available_time().

Pet: Attributes: name, species, age; Methods: update_info(), display_info().

Task: Attributes: task_name, duration, priority, completed; Methods: mark_complete(), edit_task().

Schedule: Attributes: tasks, total_time; Methods: add_task(), generate_schedule(), display_schedule().


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, after asking AI to review the skeleton logic, there were some missing relationships. I added bidirectional relationships between Owner, Pet, Task, and Schedule to establish ownership and assignment. Task now knows which pet it's for. Owner tracks their pets. Pet tracks the owner. Schedule references the owner and holds one master task list across all pets. 
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

Tradeoff: Manual Time Scheduling vs. Automatic Conflict Avoidance
 The scheduler requires users to manually specify when each task occurs rather than auto-calculating times. This means users gain control over realistic scheduling but must manage the risk of conflicts themselves as the system detects conflicts with warnings but doesn't prevent them.

Why reasonable: Pet care is tied to the owner's availability and pet routine preferences. Auto-calculated times would ignore actual availability and create schedule that may not be feasible for the owner. Manual scheduling respects real constraints while keeping owner in control.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
