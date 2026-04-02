# TC-15: Lunch Break Enforcement (Black Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Does the scheduler ever place a class during lunch (13:15-14:00)?
- **Setup**: 5 core courses, sufficient rooms.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The is_break_time_slot function correctly blocks the 13:15-14:00 lunch window. All 5 courses scheduled around the break.
