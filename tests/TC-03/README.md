# TC-03: Lab Without Lab Room (White Box)
**Category**: Room & Capacity Constraints

- **Objective**: What if a course needs a COMPUTER_LAB but only LECTURE_ROOMs exist?
- **Setup**: CS163 (L=3, P=2) with only LECTURE_ROOM available. No COMPUTER_LAB.
- **Expected**: FAIL

### Results
- **Unscheduled**: 3 components
- **Insight**: Room-type filter correctly maps LAB components to COMPUTER_LAB. Since none exist, the LAB sessions fail while proving room-type matching is strictly enforced.
