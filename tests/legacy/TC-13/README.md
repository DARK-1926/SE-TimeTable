# TC-13: Lunch Break Respect (PASS)

## Description

This test scenario ensures that the lunch break (13:15-14:00) is strictly respected for all courses. Even with a high course load (10 hours per week for a single semester), the lunch slot should remain empty in the grid.

## Expected Result

**PASS**: The course will be scheduled in all available slots EXCEPT the lunch break slot.

## Verification

1. Run TC-13.
2. Check `CSE_2` sheet in `timetable_all_departments_even.xlsx`.
3. Verify that the cell for "13:15-14:00" says "LUNCH BREAK" and is empty of courses.
