# TC-12: LEC+TUT Same Day Block (White Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Does the scheduler prevent LEC and TUT of the same course on the same day?
- **Setup**: One course (L=3, T=1), sufficient rooms and 5 weekdays.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The has_component_on_day guard successfully prevents placing a LEC and TUT on the same day. With 5 days available, the scheduler naturally distributes them across different days.
