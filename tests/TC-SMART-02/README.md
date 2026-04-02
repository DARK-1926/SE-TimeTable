# TC-SMART-02: Shared Elective Sync

- **Objective**: Force the entire dataset into a single 60-capacity room.
- **Setup**:
  - `data/combined_even.csv`: Standard full dataset.
  - `data/rooms.csv`: Only one room `C101` with capacity 60.
- **Type**: Black Box (Resource saturation).

### Results

- **Unscheduled Courses**: 18 components
- **Observation**: The single room was immediately saturated, leading to 18 unscheduled components. This confirms the system stops once physical space is exhausted.
