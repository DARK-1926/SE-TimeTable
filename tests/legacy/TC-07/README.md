# TC-07: Consecutive Slot Ordering (FAIL)

## Description

This test scenario validates **BUG-03**. A 3-hour lab session needs two consecutive 1.5-hour slots. If the slots are not sorted correctly in the internal logic, it might pick non-contiguous slots or fail to find any.

## Expected Result

**FAIL**: The scheduler may assign the lab to non-sequential slots (e.g., Slot 1 and Slot 3) or fail because it checks availability in an unsorted list of slots.

## Verification

1. Run TC-07.
2. Check `CSE_2` sheet in `timetable_all_departments_even.xlsx`.
3. Observe if the lab slots are contiguous.
