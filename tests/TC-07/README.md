# TC-07: Section A/B Split (Grey Box)
**Category**: Section & Split Constraints

- **Objective**: Do SPLIT sections get independent timetables that do not clash?
- **Setup**: CS163 Section A (Dr. Vivekraj) and Section B (Dr. Hazra), SectionMode=SPLIT.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The filter_courses_for_section logic correctly isolates Section A and B into separate scheduling passes with no faculty or room overlap.
