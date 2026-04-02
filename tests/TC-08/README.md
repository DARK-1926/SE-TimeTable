# TC-08: Faculty Preference Conflict (FAIL)

## Description

This test scenario assigns a course to `Dr. Abdul Wahid`, who has specified in `FACULTY.csv` that he is unavailable on **Monday 09:00-10:30**.

## Expected Result

**FAIL**: Currently, the scheduler DOES NOT load or respect the `preferences` column from `FACULTY.csv`. It will likely ignore the preference and schedule the course on Monday 09:00 if it's the first available slot.

## Verification

1. Run TC-08.
2. Check `CSE_2` sheet in `timetable_all_departments_even.xlsx`.
3. If `CS101` is scheduled on Monday 09:00, the test "fails" the preference check.
