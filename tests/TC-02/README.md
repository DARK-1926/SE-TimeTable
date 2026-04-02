# TC-02: Capacity Mismatch (Grey Box)
**Category**: Room & Capacity Constraints

- **Objective**: Can a 300-student class be placed in a 100-cap room?
- **Setup**: 10 courses, first one has total_students=300. Largest room is 100-cap.
- **Expected**: FAIL

### Results
- **Unscheduled**: 4 components
- **Insight**: The scheduler correctly rejects rooms that are too small. The 300-student course fails while smaller courses succeed, proving per-course capacity validation.
