# TC-04: Faculty Overload (White Box)
**Category**: Faculty & Conflict Constraints

- **Objective**: Can one professor teach 15 subjects without time conflicts?
- **Setup**: 15 unique CORE courses ALL Schedule=YES, assigned to Dr. Overloaded. 20 rooms.
- **Expected**: FAIL

### Results
- **Unscheduled**: 11 components
- **Insight**: The scheduler prevents double-booking. With 15 courses each needing L=3h + T=1h, Dr. Overloaded's weekly schedule overflows. Only ~4 courses fit, proving `check_professor_availability` works.
