# TC-02: Room Capacity Starvation (FAIL)

## Description

This test scenario assigns a course with 150 students but only provides rooms with a maximum capacity of 60.

## Expected Result

**FAIL**: The course `CS101` should remain unscheduled because no single room exists that can fit 150 students, and the scheduler (for lectures) does not support multi-room allocation.

## Verification

Check `unscheduled_courses_even.xlsx` for "No suitable room found (Needs 150 capacity)".
