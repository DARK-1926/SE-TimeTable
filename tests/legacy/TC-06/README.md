# TC-06: Elective Basket Constraint (PASS)

## Description

This test scenario ensures that the scheduler correctly handles elective baskets (B1, B2, B3). Courses within these baskets (even if for the same semester/department) should be treated as non-overlapping "synchronized" electives for the students.

## Expected Result

**PASS**: B1, B2, and B3 courses should be scheduled at different times so that students can choose any one without conflict.

## Verification

1. Run TC-06.
2. Check `CSE_2` sheet in `timetable_all_departments_even.xlsx`.
3. Verify `B1-CS121`, `B2-CS122`, and `B3-CS123` are in distinct time slots.
