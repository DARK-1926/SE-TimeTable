# TC-05: Lab Multi-Room Allocation (FAIL)

## Description

This test scenario validates **BUG-01**. A lab with 80 students is assigned, but only two labs with 40 seats each (`L105`, `L106`) are available. The scheduler should combine them.

## Expected Result

**FAIL**: Currently, the scheduler's room splitting logic is broken (`place_course_on_slots` looks for a single room first and returns `False` if not found, even if it could split for labs). It will likely report "No suitable room found (Needs 80 capacity)".

## Verification

1. Run TC-05.
2. Check `unscheduled_courses_even.xlsx` for `CS101L`.
