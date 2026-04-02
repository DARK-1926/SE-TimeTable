# TC-18: 3-Dept CE_SHARED Sync (Grey Box)
**Category**: Multi-Department Coordination

- **Objective**: Can CSE, DSAI, and ECE share MA163 in the same room at the same time?
- **Setup**: MA163 across 3 departments (total 325 students), CrossDeptGroup=CE_SHARED_1. Rooms: 350-cap + 100-cap.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The scheduler correctly aggregates 3 departments' student counts (325 total), bypasses the 100-cap room, and synchronizes all into the 350-cap room. Proves multi-department scaling.
