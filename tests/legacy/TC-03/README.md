# TC-03: Faculty Overlap (PASS)

## Description

This test scenario assigns the same faculty member (`Dr. Abdul Wahid`) to two different courses (`CS101` and `CS102`) in the same semester. The scheduler must ensure they do not overlap in time.

## Expected Result

**PASS**: Both courses should be scheduled, but at different time slots.

## Verification

Check `timetable_all_departments_even.xlsx` for `CSE_2` sheet. Verify `CS101` and `CS102` are in distinct cells and no conflict warning appeared in logs.
