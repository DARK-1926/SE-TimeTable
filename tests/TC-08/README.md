# TC-08: Combined + Split Coexistence (Grey Box)
**Category**: Section & Split Constraints

- **Objective**: Can a COMBINED course coexist with SPLIT courses in the same semester?
- **Setup**: MA163 (COMBINED) + CS163 A/B (SPLIT). Same semester.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: COMBINED courses appear on all section timetables while SPLIT courses only on their designated section. Proves SectionMode routing logic is robust.
