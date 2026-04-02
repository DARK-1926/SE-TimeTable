# TC-14: Back-to-Back LAB Stress (White Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Can 5 lab-only courses schedule without adjacent slot conflicts?
- **Setup**: 5 lab-only courses (P=2), 3 COMPUTER_LABs, 5 different faculty.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: With 5 labs and 3 lab-rooms, the adjacency guard in `find_consecutive_slots_for_minutes` correctly distributes LAB sessions across non-adjacent slots and days.
