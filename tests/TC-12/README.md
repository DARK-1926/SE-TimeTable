# TC-12: LEC+TUT Same Day Block (White Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Does the scheduler prevent LEC and TUT of the same course on the same day?
- **Setup**: One course (L=3, T=1), sufficient rooms and 5 weekdays.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `has_component_on_day` guard prevents placing LEC and TUT on the same day. With 5 days, the scheduler distributes them across different days.
