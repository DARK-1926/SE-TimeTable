# TC-17: Empty Input Resilience (Black Box)
**Category**: Input Validation & Edge Cases

- **Objective**: Does the scheduler crash on 0 courses?
- **Setup**: combined_even.csv has header row only (0 data rows).
- **Expected**: PASS (no crash, empty output)

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The scheduler gracefully handles an empty input file without crashing. No timetable is generated, no errors thrown. Proves edge case resilience.
