# TC-20: 2-Hour Lecture Block (White Box)
**Category**: Scheduling Logic & Session Planning

- **Objective**: Does L=2 produce a single 120-min block instead of two 60-min blocks?
- **Setup**: 1 course with L=2 + 1 course with L=3.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `get_lecture_session_plans` correctly generates a single 120-min block for L=2 courses. The output timetable shows one continuous 2-hour slot instead of two fragmented 1-hour slots. Proves session planning flexibility.
