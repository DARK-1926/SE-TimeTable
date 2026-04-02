# TC-NEW-03: High Strength Allocation

## Testing Type: Grey Box

### Classification: Boundary Value / Capacity Testing

### Description

Assigns 300 students to a single course ("Linear Algebra"), while the largest available room in `rooms.csv` has a capacity of only 100. This tests the capacity matching logic in `find_suitable_room_for_slot`.

### How to Run

```bash
python tests/run_test.py --tc TC-NEW-03
```

### Actual Output (Verified)

- **Unscheduled Courses**: 14
- **Findings**: The 300-student course was correctly identified as unschedulable due to the lack of a suitable large room.
