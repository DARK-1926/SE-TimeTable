# TC-15: Large Batch Room Fallback (PASS)

## Description

This test scenario ensures that a very large batch (200 students) is correctly assigned to the only room that can fit it: `C004` (capacity 240).

## Expected Result

**PASS**: The course `MA163` should be scheduled automatically in `C004`.

## Verification

1. Run TC-15.
2. Check `CSE_2` sheet in `timetable_all_departments_even.xlsx`.
3. Verify `MA163` is in room `C004`.
4. Check `unscheduled_courses_even.xlsx` to ensure it is not listed there.
