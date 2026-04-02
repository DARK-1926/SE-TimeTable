# TC-SMART-04: Departmental Isolation (Room Type Fail)

- **Objective**: Test department-specific scheduling when no rooms of the required type are available.
- **Setup**:
  - `data/combined_even.csv`: Standard head of `combined1.csv`.
  - `data/rooms.csv`: Room `C101` exists but its type is `WRONG_TYPE`.
- **Type**: Black Box (Type constraint).

### Results

- **Unscheduled Courses**: 19 components
- **Observation**: All 19 components failed because the scheduler could not find a room matching the required 'LECTURE_ROOM' type.
