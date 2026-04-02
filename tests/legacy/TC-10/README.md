# TC-10: Max Slot Load (FAIL)

## Description

This test scenario overwhelms the scheduler by providing 60 lecture courses for a single department (`CSE_2`). Given there are only ~50 valid time slots in a week (5 days \* 10 slots), some courses MUST remain unscheduled.

## Expected Result

**FAIL**: The scheduler should schedule as many as possible (~50) and leave the rest in the `unscheduled_courses_even.xlsx` with the reason "No suitable slot found".

## Verification

1. Run TC-10.
2. Check `unscheduled_courses_even.xlsx`. It should contain at least 10 courses.
