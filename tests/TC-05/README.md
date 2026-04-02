# TC-05: Multi-Faculty Parsing (Black Box)
**Category**: Faculty & Conflict Constraints

- **Objective**: Does the scheduler correctly parse Dr. Alpha & Dr. Beta as two faculty?
- **Setup**: Course 1: Faculty=Dr. Alpha & Dr. Beta. Course 2: Faculty=Dr. Alpha.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The select_faculty function correctly splits multi-faculty strings. Both courses scheduled without conflicts.
