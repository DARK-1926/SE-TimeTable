# TC-06: Ghost Faculty (Black Box)
**Category**: Faculty & Conflict Constraints

- **Objective**: What if a course has NO faculty assigned (empty, NaN, or TBD)?
- **Setup**: 3 courses with Faculty = empty, NaN, and "TBD".
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The scheduler gracefully handles missing faculty by defaulting to "TBD". All 3 courses scheduled successfully. Proves defensive input handling.
