# TC-SMART-01: Hallway Jam (Large Classes)

- **Objective**: Squeeze multiple high-strength classes (230 students) into the only available large hall (C004, capacity 240).
- **Setup**:
  - `data/combined_even.csv`: 15 courses with 230 students each.
  - `data/rooms.csv`: Only one room `C004` with capacity 240.
- **Type**: Black Box (Stressing a single high-capacity resource).

### Results

- **Unscheduled Courses**: 2 components
- **Observation**: The system successfully scheduled 43 out of 45 sessions into the single hall, proving efficient slot utilization for large groups.
