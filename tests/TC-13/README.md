# TC-13: Student Timeline Saturation (Black Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Can a student attend 20 core subjects in one semester?
- **Setup**: 20 unique CORE courses for CSE Sem 4. 20 rooms available.
- **Expected**: FAIL

### Results
- **Unscheduled**: 8 components
- **Insight**: 20 core subjects generate ~50+ weekly sessions that cannot fit a ~35-hour student schedule. Human time is the ultimate hard constraint, beyond rooms or faculty.
