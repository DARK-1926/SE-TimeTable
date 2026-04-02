"""Write READMEs for all 20 test cases."""
import os

readmes = {
'TC-01': """# TC-01: Room Starvation (Black Box)
**Category**: Room & Capacity Constraints

- **Objective**: What happens when 144 courses compete for just 2 small rooms?
- **Setup**: Full combined1.csv (144 courses), only 2 LECTURE_ROOM (60 cap each).
- **Expected**: FAIL

### Results
- **Unscheduled**: 16 components
- **Insight**: The scheduler does not crash under extreme room deficit. It schedules what fits and gracefully reports the rest. Proves robust error handling under resource starvation.
""",

'TC-02': """# TC-02: Capacity Mismatch (Grey Box)
**Category**: Room & Capacity Constraints

- **Objective**: Can a 300-student class be placed in a 100-cap room?
- **Setup**: 10 courses, first one has total_students=300. Largest room = 100 cap.
- **Expected**: FAIL

### Results
- **Unscheduled**: 4 components
- **Insight**: The scheduler rejects rooms that are too small. The 300-student course fails while smaller ones succeed. Proves per-course capacity validation via `find_suitable_room_for_slot`.
""",

'TC-03': """# TC-03: Lab Without Lab Room (White Box)
**Category**: Room & Capacity Constraints

- **Objective**: What if a course needs a COMPUTER_LAB but only LECTURE_ROOMs exist?
- **Setup**: CS163 (L=3, P=2) with only LECTURE_ROOM. No COMPUTER_LAB in rooms.csv.
- **Expected**: FAIL

### Results
- **Unscheduled**: 1 component (LAB)
- **Insight**: Room-type filter maps LAB components to COMPUTER_LAB. Since none exist, the LAB session fails while LEC passes. Proves room-type matching is strictly enforced.
""",

'TC-04': """# TC-04: Faculty Overload (White Box)
**Category**: Faculty & Conflict Constraints

- **Objective**: Can one professor teach 15 subjects without time conflicts?
- **Setup**: 15 unique CORE courses ALL Schedule=YES, assigned to Dr. Overloaded. 20 rooms.
- **Expected**: FAIL

### Results
- **Unscheduled**: 11 components
- **Insight**: The scheduler prevents double-booking. With 15 courses each needing L=3h + T=1h, Dr. Overloaded's weekly schedule overflows. Only ~4 courses fit, proving `check_professor_availability` works.
""",

'TC-05': """# TC-05: Multi-Faculty Parsing (Black Box)
**Category**: Faculty & Conflict Constraints

- **Objective**: Does the scheduler correctly parse "Dr. Alpha & Dr. Beta" as two faculty?
- **Setup**: Course 1: Faculty="Dr. Alpha & Dr. Beta". Course 2: Faculty="Dr. Alpha".
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `select_faculty` correctly splits multi-faculty strings. Both courses scheduled without conflicts, proving the '&' delimiter parsing works.
""",

'TC-06': """# TC-06: Ghost Faculty (Black Box)
**Category**: Faculty & Conflict Constraints

- **Objective**: What if a course has NO faculty assigned (empty, NaN, or TBD)?
- **Setup**: 3 courses with Faculty = empty, NaN, and "TBD".
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The scheduler gracefully handles missing faculty by defaulting to "TBD". All 3 courses scheduled successfully. Proves defensive input handling.
""",

'TC-07': """# TC-07: Section A/B Split (Grey Box)
**Category**: Section & Split Constraints

- **Objective**: Do SPLIT sections get independent timetables without clashes?
- **Setup**: CS163 Section A (Dr. Vivekraj) and Section B (Dr. Hazra).
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `filter_courses_for_section` isolates Section A and B into separate scheduling passes. Each section gets its own timetable with no faculty or room overlap.
""",

'TC-08': """# TC-08: Combined + Split Coexistence (Grey Box)
**Category**: Section & Split Constraints

- **Objective**: Can a COMBINED course coexist with SPLIT courses in the same semester?
- **Setup**: MA163 (COMBINED) + CS163 A/B (SPLIT). Same semester.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: COMBINED courses appear on all section timetables while SPLIT courses only on their designated section. Proves SectionMode routing logic is robust.
""",

'TC-09': """# TC-09: Basket Slot Locking (White Box)
**Category**: Elective Basket & Cross-Dept

- **Objective**: Do all B1 electives land on the same time slot?
- **Setup**: 3 courses with B1- prefix, same semester.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `schedule_global_elective_baskets` correctly locks shared time slots for all B1 courses. Students can pick any B1 elective without schedule conflicts.
""",

'TC-10': """# TC-10: Cross-Dept Shared Room (Grey Box)
**Category**: Elective Basket & Cross-Dept

- **Objective**: Can CSE and DSAI share a class in the same room at the same time?
- **Setup**: Shared Discrete Math (CSE=90, DSAI=90). Rooms: 100-cap and 200-cap.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `CrossDeptGroup` logic synchronizes two departments into the 200-cap room at the same slot, bypassing the too-small 100-cap room.
""",

'TC-11': """# TC-11: Multi-Basket vs Core Competition (Black Box)
**Category**: Elective Basket & Cross-Dept

- **Objective**: Can 5 cores + 3 basket types (B1, B2, B4) all fit without conflicts?
- **Setup**: 5 core courses + B1(3 courses) + B2(2 courses) + B4(1 course). Limited rooms.
- **Expected**: PARTIAL FAIL

### Results
- **Unscheduled**: 2 components
- **Insight**: With 5 heavy cores and 3 different basket types competing, the timeline overflows slightly. The scheduler correctly prioritizes cores but cannot fit all basket sessions. Proves basket scheduling respects core course priority.
""",

'TC-12': """# TC-12: LEC+TUT Same Day Block (White Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Does the scheduler prevent LEC and TUT of the same course on the same day?
- **Setup**: One course (L=3, T=1), sufficient rooms and 5 weekdays.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `has_component_on_day` guard prevents placing LEC and TUT on the same day. With 5 days, the scheduler distributes them across different days.
""",

'TC-13': """# TC-13: Student Timeline Saturation (Black Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Can a student attend 20 core subjects in one semester?
- **Setup**: 20 unique CORE courses for CSE Sem 4. 20 rooms available.
- **Expected**: FAIL

### Results
- **Unscheduled**: 8 components
- **Insight**: 20 core subjects generate ~50+ weekly sessions that cannot fit a ~35-hour student schedule. Human time is the ultimate hard constraint, beyond rooms or faculty.
""",

'TC-14': """# TC-14: Back-to-Back LAB Stress (White Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Can 5 lab-only courses schedule without adjacent slot conflicts?
- **Setup**: 5 lab-only courses (P=2), 3 COMPUTER_LABs, 5 different faculty.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: With 5 labs and 3 lab-rooms, the adjacency guard in `find_consecutive_slots_for_minutes` correctly distributes LAB sessions across non-adjacent slots and days.
""",

'TC-15': """# TC-15: Lunch Break Enforcement (Black Box)
**Category**: Temporal & Adjacency Constraints

- **Objective**: Does the scheduler ever place a class during lunch (13:15-14:00)?
- **Setup**: 5 core courses, 10 rooms.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `is_break_time_slot` correctly blocks the lunch window. All courses scheduled around the break, proving temporal exclusion zones are respected.
""",

'TC-16': """# TC-16: Schedule=NO Filter (White Box)
**Category**: Input Validation & Edge Cases

- **Objective**: Does the scheduler correctly skip courses marked Schedule=NO?
- **Setup**: 1 course with Schedule=YES, 2 courses with Schedule=NO.
- **Expected**: PASS (only 1 course appears in output)

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: Courses with Schedule=NO are silently filtered out before scheduling begins. Only the YES course appears in the generated timetable. Proves input pre-processing works correctly.
""",

'TC-17': """# TC-17: Empty Input Resilience (Black Box)
**Category**: Input Validation & Edge Cases

- **Objective**: Does the scheduler crash on 0 courses?
- **Setup**: combined_even.csv has header row only (0 data rows).
- **Expected**: PASS (no crash, empty output)

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The scheduler gracefully handles an empty input file without crashing. No timetable is generated, no errors thrown. Proves edge case resilience.
""",

'TC-18': """# TC-18: 3-Dept CE_SHARED Sync (Grey Box)
**Category**: Multi-Department Coordination

- **Objective**: Can CSE, DSAI, and ECE share MA163 in the same room at the same time?
- **Setup**: MA163 across 3 departments (total 325 students), CrossDeptGroup=CE_SHARED_1. Rooms: 350-cap + 100-cap.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The scheduler correctly aggregates 3 departments' student counts (325 total), bypasses the 100-cap room, and synchronizes all into the 350-cap room. Proves multi-department scaling.
""",

'TC-19': """# TC-19: Room Reuse Across Semesters (White Box)
**Category**: Resource Sharing & Isolation

- **Objective**: Can Semester 2 and Semester 4 share a single room without conflicts?
- **Setup**: 2 courses in Sem 2 + 2 courses in Sem 4, only 1 room (60-cap).
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: The room_schedule is global, so Sem 2 and Sem 4 courses correctly compete for the same room. Since students in different semesters don't overlap, the scheduler can slot them at the same time on different days, proving cross-semester room reuse.
""",

'TC-20': """# TC-20: 2-Hour Lecture Block (White Box)
**Category**: Scheduling Logic & Session Planning

- **Objective**: Does L=2 produce a single 120-min block instead of two 60-min blocks?
- **Setup**: 1 course with L=2 + 1 course with L=3.
- **Expected**: PASS

### Results
- **Unscheduled**: 0 (Pass)
- **Insight**: `get_lecture_session_plans` correctly generates a single 120-min block for L=2 courses. The output timetable shows one continuous 2-hour slot instead of two fragmented 1-hour slots. Proves session planning flexibility.
""",
}

for tc, content in readmes.items():
    path = f'tests/{tc}/README.md'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written {path}')
print('All 20 READMEs created.')
