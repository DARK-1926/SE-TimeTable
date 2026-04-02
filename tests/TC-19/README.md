# TC-19: Room Reuse Across Semesters (White Box)
**Category**: Resource Sharing & Isolation

- **Objective**: Can Semester 2 and Semester 4 share a single room without conflicts?
- **Setup**: 2 courses in Sem 2 + 2 courses in Sem 4, only 1 room (60-cap).
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The room_schedule is global, so Sem 2 and Sem 4 courses correctly compete for the same room. Since students in different semesters don't overlap, the scheduler can slot them at the same time on different days, proving cross-semester room reuse.
