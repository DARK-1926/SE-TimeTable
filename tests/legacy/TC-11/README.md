# TC-11: Room Leakage / Double Booking (FAIL)

## Description

This test scenario validates **BUG-02**. By providing only one lecture room for two different courses, the scheduler should ideally place them in different slots. However, due to `find_suitable_room_for_slot` not actualy updating the global schedule while searching, it might return the same room for two courses at the same time.

## Expected Result

**FAIL**: Both courses `CS101` and `DS101` might be scheduled at the same time in room `C101`.

## Verification

1. Run TC-11.
2. Check `timetable_all_departments_even.xlsx`.
3. Compare `CSE_2` and `DSAI_2` sheets. Check if they have classes in the same slot and room.
