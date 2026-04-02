# TC-11: Elective vs Core Priority (Black Box)
**Category**: Elective Basket & Cross-Dept

- **Objective**: Does the scheduler always prioritize core courses over electives?
- **Setup**: 2 core courses + 3 B1 electives, same semester, limited rooms.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: Core courses are processed before elective baskets. Even with limited rooms, all courses fit because the scheduler correctly orders its scheduling passes.
