# TC-SMART-03: Student Schedule Starvation (CORE ONLY)

- **Objective**: Mathematically overload a single semester's curriculum using unique CORE courses to exceed the available weekly time slots.
- **Setup**:
  - `data/combined_even.csv`: 20 CORE subjects (no baskets) assigned to CSE Semester 4.
  - `data/rooms.csv`: Provided 20 rooms (ample space).
- **Type**: Black Box (Testing student-side availability limits).

### Results

- **Unscheduled Courses**: 13 components
- **Observation**: This test proves that the "Human Constraint" (student time) is a hard limit. Even with infinite rooms, the system correctly unschedules 13 sessions because the student's 5-day timeline is completely saturated.
