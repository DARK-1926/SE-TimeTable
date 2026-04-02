# TC-16: Schedule=NO Filter (White Box)
**Category**: Input Validation & Edge Cases

- **Objective**: Does the scheduler correctly skip courses marked Schedule=NO?
- **Setup**: 1 course with Schedule=YES, 2 courses with Schedule=NO.
- **Expected**: PASS (only 1 course appears in output)

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: Courses with Schedule=NO are silently filtered out before scheduling begins. Only the YES course appears in the generated timetable. Proves input pre-processing works correctly.
