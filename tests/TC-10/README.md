# TC-10: Cross-Dept Shared Room (Grey Box)
**Category**: Elective Basket & Cross-Dept

- **Objective**: Can CSE and DSAI share a class in the same room at the same time?
- **Setup**: Shared Discrete Math (CSE=90, DSAI=90). Rooms: 100-cap and 200-cap.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `CrossDeptGroup` logic synchronizes two departments into the 200-cap room at the same slot, bypassing the too-small 100-cap room.
