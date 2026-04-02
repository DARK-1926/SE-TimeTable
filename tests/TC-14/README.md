# TC-14: Back-to-Back LAB Prevention (White Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Are two LAB sessions ever placed in adjacent time slots?
- **Setup**: 2 courses (P=2 each), sufficient lab rooms and days.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The adjacency guard in find_consecutive_slots_for_minutes correctly prevents two LAB components from being placed back-to-back.
