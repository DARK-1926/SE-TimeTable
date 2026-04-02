# TC-14: Malformed CSV Resilience (PASS/FAIL)

## Description

This test scenario ensures that the scheduler doesn't crash on slightly malformed CSV data, such as missing student count or extra whitespace.

## Expected Result

**PASS/FAIL**: The system should handle missing student count by defaulting to 50 (PASS). However, it might still have issues with other malformed fields.

## Verification

1. Run TC-14.
2. Check if the scheduler finishes without a crash.
