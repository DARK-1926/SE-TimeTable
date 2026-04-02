# TC-07: Section A/B Split (Grey Box)
**Category**: Section & Split Constraints

- **Objective**: Do SPLIT sections get independent timetables without clashes?
- **Setup**: CS163 Section A (Dr. Vivekraj) and Section B (Dr. Hazra).
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `filter_courses_for_section` isolates Section A and B into separate scheduling passes. Each section gets its own timetable with no faculty or room overlap.
