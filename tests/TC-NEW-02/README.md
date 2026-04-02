# TC-NEW-02: Faculty Overload

## Testing Type: White Box

### Classification: Conflict Resolution Testing

### Description

This test assigns over 15 different course components to a single faculty member ("Dr. Anand Barangi"). It tests the internal `professor_schedule` logic and its ability to handle near-impossible faculty constraints.

### How to Run

```bash
python tests/run_test.py --tc TC-NEW-02
```

### Actual Output (Verified)

- **Unscheduled Courses**: 9
- **Findings**: Faculty "Dr. Anand Barangi" had a packed schedule. Many courses were unscheduled with the reason "Professor busy" or "Could not place LEC".
