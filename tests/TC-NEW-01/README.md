# TC-NEW-01: Room Capacity Starvation

## Testing Type: Black Box

### Classification: Resource Constraint Testing

### Description

This test uses the full course list from `combined1.csv` but restricts the available rooms to just 2 `LECTURE_ROOM`s (C101 and C102).

### How to Run

```bash
python tests/run_test.py --tc TC-NEW-01
```

### Actual Output (Verified)

- **Unscheduled Courses**: 17
- **Findings**: The system correctly identified most courses as unschedulable but successfully placed a subset in the available slots without crashing.
