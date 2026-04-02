# TC-03: Lab Without Lab Room (White Box)
**Category**: Room & Capacity Constraints

- **Objective**: What if a course needs a COMPUTER_LAB but only LECTURE_ROOMs exist?
- **Setup**: CS163 (L=3, P=2) with only LECTURE_ROOM. No COMPUTER_LAB in rooms.csv.
- **Expected**: FAIL

### Results
- **Unscheduled**: 1 component (LAB)
- **Insight**: Room-type filter maps LAB components to COMPUTER_LAB. Since none exist, the LAB session fails while LEC passes. Proves room-type matching is strictly enforced.
