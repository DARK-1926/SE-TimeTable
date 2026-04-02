# TC-04: Faculty Overload (White Box)
**Category**: Faculty & Conflict Constraints

- **Objective**: Can one professor teach 15 different subjects without time conflicts?
- **Setup**: 15 CORE courses all assigned to Dr. Overloaded. Plenty of rooms.
- **Expected**: FAIL

### Results
- **Unscheduled**: 9 components
- **Insight**: The scheduler correctly prevents a single faculty member from being in two places at once. Only 6 of 15 courses fit into the professors weekly schedule.
