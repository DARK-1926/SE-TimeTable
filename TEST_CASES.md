# Automated Time-Table Scheduler — Test Case Report

This report summarizes the 15 test scenarios designed to validate the scheduler's logic and document its known failure modes.

## Summary Table

| ID        | Title                      | Expected | Actual (Current Code) | Status | Key Findings                                                         |
| --------- | -------------------------- | -------- | --------------------- | ------ | -------------------------------------------------------------------- |
| **TC-01** | Ideal Schedule             | PASS     | PASS                  | ✅     | Basic logic is sound for low loads.                                  |
| **TC-02** | Room Capacity Starvation   | FAIL     | FAIL                  | ✅     | Correctly identifies when no single room is large enough.            |
| **TC-03** | Faculty Overlap            | PASS     | PASS                  | ✅     | Scheduler moves faculty to different slots to avoid clash.           |
| **TC-04** | CE-shared Bug              | PASS     | **FAIL**              | ❌     | **BUG-07 confirmed**: Shared courses fail for 2nd department.        |
| **TC-05** | Lab Multi-Room Allocation  | PASS     | **FAIL**              | ❌     | **BUG-01 confirmed**: Fails to split large labs into multiple rooms. |
| **TC-06** | Elective Basket Constraint | PASS     | PASS                  | ✅     | B1/B2/B3 baskets are correctly synchronized.                         |
| **TC-07** | Consecutive Slot Ordering  | PASS     | **FAIL**              | ❌     | **BUG-03 confirmed**: Long sessions may use unsorted slots.          |
| **TC-08** | Faculty Preference         | PASS     | **FAIL**              | ❌     | System ignores "preferences" column in FACULTY.csv.                  |
| **TC-09** | Section Splitting          | PASS     | PASS                  | ✅     | A/B sections of the same course handled correctly.                   |
| **TC-10** | Max Slot Load              | FAIL     | FAIL                  | ✅     | Identifies when the week is over-saturated.                          |
| **TC-11** | Double Booking             | FAIL     | **FAIL**              | ❌     | **BUG-02 confirmed**: Two courses can book the same room.            |
| **TC-12** | Faculty Alias Conflict     | FAIL     | **FAIL**              | ❌     | **BUG-06 confirmed**: Typos in names bypass clash detection.         |
| **TC-13** | Lunch Break Respect        | PASS     | PASS                  | ✅     | Lunch slot is correctly reserved across all sheets.                  |
| **TC-14** | Malformed CSV Resilience   | PASS     | PASS                  | ✅     | System defaults missing student strengths to 50.                     |
| **TC-15** | Large Room Fallback        | PASS     | PASS                  | ✅     | Correctly identifies C004 as the only fit for 200 students.          |

## Replication Instructions

Each test case is located in its own subfolder under `tests/`. To replicate a specific test case:

1. Use the provided `run_test.py` script:
   ```bash
   python tests/run_test.py --tc TC-04
   ```
2. The script will:
   - Copy the test data to the `data/` folder.
   - Run the scheduler script.
   - Save the Excel results to `tests/TC-XX/results/`.
   - Print whether the test "Passed" or "Failed" based on unscheduled courses.

## Detailed Reports

Individual `README.md` files for each test case can be found in their respective directories:

- [TC-01 README](file:///c:/Users/mohit/Downloads/SE%20TT/Automated-Time-Table-Scheduling-at-IIIT-Dharwad/tests/TC-01/README.md)
- [TC-04 README (CE-shared)](file:///c:/Users/mohit/Downloads/SE%20TT/Automated-Time-Table-Scheduling-at-IIIT-Dharwad/tests/TC-04/README.md)
- [TC-11 README (Double Booking)](file:///c:/Users/mohit/Downloads/SE%20TT/Automated-Time-Table-Scheduling-at-IIIT-Dharwad/tests/TC-11/README.md)
