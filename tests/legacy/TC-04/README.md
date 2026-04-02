# TC-04: CE-shared Bug (FAIL)

## Description

This test scenario validates **BUG-07**. `MA163` is shared between `CSE` and `DSAI` via the `CE_SHARED_1` group. Both departments should have the same course in the same slot.

## Expected Result

**FAIL**: Due to the synchronization bug, the course will be scheduled for the FIRST department (CSE) but will be MISSING from the second department's (DSAI) timetable grid, even though it appears in the legend.

## Verification

1. Run TC-04.
2. Check `DSAI_2` sheet in `timetable_all_departments_even.xlsx`.
3. Search for `MA163` in the calendar grid. It will likely be missing.
