# TC-09: Section Splitting (PASS)

## Description

This test scenario ensures that the scheduler correctly handles courses that are split into sections (A and B). Each section should get its own slot even if they share the same course code.

## Expected Result

**PASS**: Both `Section A` and `Section B` should be scheduled at different times (or the same time if they have different faculty and rooms are available).

## Verification

1. Run TC-09.
2. Check `CSE_2_Section_A` and `CSE_2_Section_B` (or the respective sheets) in `timetable_all_departments_even.xlsx`.
3. They should both be fully scheduled.
