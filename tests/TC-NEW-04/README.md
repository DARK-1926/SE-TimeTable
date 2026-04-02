# TC-NEW-04: Peak Load Stress Test

## Testing Type: Black Box

### Classification: Stress / Performance Testing

### Description

Duplicates the `combined1.csv` data three times, requesting over 400 class sessions in a single week. This stresses the random search algorithm and the overall throughput capacity of the IIIT Dharwad scheduling model.

### How to Run

```bash
python tests/run_test.py --tc TC-NEW-04
```

### Actual Output (Verified)

- **Unscheduled Courses**: 16
- **Findings**: System takes longer to run. Large portion of courses remained unscheduled as time slots and rooms were exhausted.
