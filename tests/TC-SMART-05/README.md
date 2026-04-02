# TC-SMART-05: Cross-Departmental Synchronization

- **Objective**: Synchronize a shared course between CSE and DSAI while enforcing combined capacity.
- **Setup**:
  - `data/combined_even.csv`: Shared "Discrete Math" for CSE (90) and DSAI (90). Total needed: 180.
  - `data/rooms.csv`: R101 (100 cap) and R202 (200 cap).
- **Type**: Grey Box (Testing synchronized multi-dept allocation).

### Results

- **Unscheduled Courses**: 0 (Pass)
- **Observation**: The system successfully bypassed the too-small R101, combined the student strengths of both departments (180), and scheduled them into R202 at the exact same time slot. This confirms the cross-departmental shared resource logic is fully functional.
