# TC-09: Basket Slot Locking (White Box)
**Category**: Elective Basket & Cross-Dept

- **Objective**: Do all B1 electives land on the same time slot?
- **Setup**: 3 courses with B1- prefix, same semester.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `schedule_global_elective_baskets` correctly locks shared time slots for all B1 courses. Students can pick any B1 elective without schedule conflicts.
