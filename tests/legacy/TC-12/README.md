# TC-12: Faculty Alias Conflict (FAIL)

## Description

This test scenario validates **BUG-06**. The same faculty member is assigned two courses, but their name is spelled slightly differently (e.g., `Dr. Abdul Wahid` vs `Dr. Abdulwahid`).

## Expected Result

**FAIL**: The scheduler treats them as different people and might schedule them at the same time, leading to a physical impossibility for the faculty member.

## Verification

1. Run TC-12.
2. Check `teacher_timetables_even.xlsx`.
3. Observe two separate sheets for `Dr. Abdul Wahid` and `Dr. Abdulwahid`.
4. Check if they have class at the same time in the same room (if room allows) or different rooms.
