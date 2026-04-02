# TC-13: Student Timeline Saturation (Black Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Can a student attend 20 core subjects in one semester?
- **Setup**: 20 unique CORE courses for CSE Sem 4. 20 rooms available.
- **Expected**: FAIL

### Results
- **Unscheduled**: 8 components
- **Insight**: Even with ample rooms, 20 core subjects generate ~50+ weekly sessions that cannot fit into a students ~35-hour schedule. This proves student availability is the hardest constraint.
