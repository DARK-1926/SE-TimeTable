# TC-15: Lunch Break Enforcement (Black Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Does the scheduler ever place a class during lunch (13:15-14:00)?
- **Setup**: 5 core courses, 10 rooms.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `is_break_time_slot` correctly blocks the lunch window. All courses scheduled around the break, proving temporal exclusion zones are respected.
