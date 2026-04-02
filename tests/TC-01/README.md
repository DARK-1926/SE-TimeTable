# TC-01: Room Starvation (Black Box)
**Category**: Room & Capacity Constraints

- **Objective**: What happens when 144 courses compete for just 2 small rooms?
- **Setup**: Full combined1.csv (144 courses), only 2 LECTURE_ROOM (60 cap each).
- **Expected**: FAIL

### Results
- **Unscheduled**: 16 components
- **Insight**: The scheduler does not crash under extreme room deficit. It successfully schedules what fits and gracefully reports the rest as unschedulable.
