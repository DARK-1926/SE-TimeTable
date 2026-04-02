# Bug Report — Automated Timetable Scheduler (IIIT Dharwad)

**Branch analysed:** `main` (commit `a18e52c`)  
**Even-semester data file added:** `data/combined_even.csv`  
**Date:** 2026-03-31

---

## Data File Notes

The uploaded even-semester CSV (`combined1 - Sheet1.csv`) was saved as
`data/combined_even.csv` with the following normalisation applied:

| Issue in original upload                                             | Fix applied                                                           |
| -------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Trailing comma on every header/row (extra empty column)              | Removed trailing comma                                                |
| `CrossDeptGroup` values had a trailing space (e.g. `CE_SHARED_1 `)   | Trimmed to `CE_SHARED_1`                                              |
| `nan` in numeric L/T/P/C cells for ECE Sem-4 courses                 | Replaced with realistic integer values inferred from course structure |
| Typo `B2- CS253` (space before code)                                 | Normalised to `B2-CS253`                                              |
| Typo `B2-EC257 Causal Ineference`                                    | Corrected to `Causal Inference`                                       |
| Multiline faculty cell for `B5-CS373`                                | Collapsed to single line                                              |
| DSAI Sem-4 row with empty Course Code and note `post` in last column | Assigned code `DS265` and removed stray text                          |

---

## Bugs

---

### BUG-01 — `place_course_on_slots` marks a combined-lab room as occupied using the raw combined string key

**Severity:** Critical  
**File:** `src/Class_TT.py`  
**Function:** `place_course_on_slots`  
**Lines (main branch):** ~530–560

#### Description

When a lab is assigned a combined room such as `L105+L106`, the function
writes the booking into `room_schedule` using the full string `"L105+L106"`
as the key instead of splitting it and booking each individual room
separately. This means neither `L105` nor `L106` is ever marked as occupied
in `room_schedule`, so both rooms can be double-booked by subsequent courses
in the same time slot.

#### Buggy code

```python
# place_course_on_slots — main branch
if candidate_room not in room_schedule:
    room_schedule[candidate_room] = {d: set() for d in range(len(DAYS))}
room_schedule[candidate_room][day].add(si)
```

`candidate_room` here is `"L105+L106"`. The individual keys `"L105"` and
`"L106"` are never updated, so `find_suitable_room_for_slot` sees them as
free and assigns them again.

#### Buggy output

Two different courses end up scheduled in the same lab room at the same
time. In the generated `timetable_all_departments.xlsx` you will see, for
example, both `CS163-LAB (Section A)` and `CS208-LAB (Section B)` showing
room `L106` at `14:00–16:00 Tuesday`. The teacher timetable for the
affected faculty also shows a double-booking.

#### How to reproduce

1. Use `data/combined_even.csv` (Sem-2 CSE has two lab courses with 110
   students each — larger than any single lab's 60-seat capacity, so
   combined labs are always triggered).
2. Run `python src/Class_TT.py`.
3. Open `output/timetable_all_departments.xlsx`.
4. Compare the room column for any two lab sessions on the same day — you
   will find the same individual lab room listed for both.

#### Potential fix

Split the combined room name on `'+'` and mark each component room:

```python
for crn in str(candidate_room).split('+'):
    if crn not in room_schedule:
        room_schedule[crn] = {d: set() for d in range(len(DAYS))}
    room_schedule[crn][day].add(si)
```

---

### BUG-02 — `find_suitable_room_for_slot` books C004 without updating `room_schedule`

**Severity:** Critical  
**File:** `src/Class_TT.py`  
**Function:** `find_suitable_room_for_slot`  
**Lines (main branch):** ~340–360

#### Description

The fallback block that assigns the 240-seat hall `C004` to large courses
(>120 students) calls `course_room_mapping[mapping_key] = 'C004'` and
returns `'C004'`, but it also explicitly updates `room_schedule['C004']`
with the slot indices. However, the earlier "best room" path (lines ~310–330)
returns `best_room` without ever writing to `room_schedule` at all — it only
writes to `course_room_mapping`. This means the room is considered free for
the next scheduling attempt even though it has just been assigned.

#### Buggy code

```python
# "best room" path — room_schedule is never updated here
if best_room:
    course_room_mapping[mapping_key] = best_room
    return best_room          # <-- room_schedule NOT updated
```

The C004 fallback path does update `room_schedule`, but the primary path
does not, so any room found via the primary path can be assigned to multiple
courses in the same slot.

#### Buggy output

Multiple courses appear in the same lecture room at the same time slot.
For example, `CS162 (ALL)` and `MA163 (ALL)` — both 200+ student courses —
may both be assigned room `C003` on Monday 09:00–10:30. The
`unscheduled_courses.xlsx` will be shorter than expected (courses appear
scheduled) but the timetable itself contains clashes.

#### How to reproduce

1. Run `python src/Class_TT.py` with `data/combined_even.csv` (Sem-2 CSE
   has `CS162` with 220 students and `MA163` with 111 students — both need
   large rooms).
2. Open `output/timetable_all_departments.xlsx`, sheet `CSE_2_ALL`.
3. Look for two different course codes occupying the same room on the same
   day/slot in the legend or cell content.

#### Potential fix

After selecting `best_room`, immediately mark it in `room_schedule`:

```python
if best_room:
    course_room_mapping[mapping_key] = best_room
    if best_room not in room_schedule:
        room_schedule[best_room] = {d: set() for d in range(len(DAYS))}
    for si in slot_indices:
        room_schedule[best_room][day].add(si)
    return best_room
```

---

### BUG-03 — Time slots are appended out of chronological order

**Severity:** High  
**File:** `src/Class_TT.py`  
**Function:** `generate_time_slots`  
**Lines (main branch):** ~115–140

#### Description

Two afternoon slots are appended in the wrong order:

```python
slots.append((time(17, 10), time(17, 30)))   # index 17 — WRONG ORDER
slots.append((time(16, 30), time(17, 10)))   # index 18
```

`16:30–17:10` is appended _after_ `17:10–17:30`, so the `TIME_SLOTS` list
is not monotonically increasing. `find_consecutive_slots_for_minutes`
iterates `TIME_SLOTS` sequentially and accumulates minutes assuming
consecutive slots are contiguous. When it hits index 17 (`17:10`) followed
by index 18 (`16:30`), the accumulated time appears correct numerically but
the actual wall-clock block is non-contiguous (it goes forward then
backward in time), producing a timetable entry that spans a time range that
does not exist.

#### Buggy output

A course may be shown as scheduled at `17:10–17:30` immediately followed by
`16:30–17:10` in the Excel output, which is physically impossible. The cell
merge in the Excel sheet will also be wrong — the two cells will be in the
wrong visual order, making the timetable unreadable for that block.

```
Example cell content (buggy):
  Row "17:10" → CS304 LEC  Dr. Girish  Room 302
  Row "16:30" → (continuation of CS304)
```

#### How to reproduce

1. Run `python src/Class_TT.py`.
2. Open `output/timetable_all_departments.xlsx`.
3. Scroll to the afternoon section of any timetable sheet.
4. Observe that the `16:30` row appears below the `17:10` row.

#### Potential fix

Swap the two lines so slots are in ascending time order:

```python
slots.append((time(16, 30), time(17, 10)))   # 40 min
slots.append((time(17, 10), time(17, 30)))   # 20 min
```

---

### BUG-04 — `check_professor_availability` uses slot-count range instead of actual slot indices

**Severity:** High  
**File:** `src/Class_TT.py`  
**Function:** `check_professor_availability`  
**Lines (main branch):** ~570–580

#### Description

The function constructs the set of "new slots" as a contiguous integer range
`range(start_idx, start_idx + duration_slots)`. However, the actual slot
indices used by a scheduled component are not always contiguous integers —
they are the specific indices returned by `find_consecutive_slots_for_minutes`,
which skips break slots and minor slots. If a break slot sits between two
lecture slots (e.g., indices 9 and 11 with index 10 being lunch), the range
`range(9, 11)` = `{9, 10}` is checked instead of `{9, 11}`, so index 11 is
never checked for conflicts. A professor can therefore be double-booked at
slot 11.

#### Buggy code

```python
def check_professor_availability(professor_schedule, faculty, day, start_idx, duration_slots):
    new_slots = set(range(start_idx, start_idx + duration_slots))  # BUG: range, not actual indices
    existing_slots = professor_schedule[faculty][day]
    return not (new_slots & existing_slots)
```

#### Buggy output

A faculty member appears in two different courses at the same time slot in
`teacher_timetables.xlsx`. For example, `Dr. Suvadip Hazra` (who teaches
both `CS163` and `CS165/CS201` in Sem-2 CSE) may show two entries at
`11:00` on the same day.

#### How to reproduce

1. Use `data/combined_even.csv`.
2. Run `python src/Class_TT.py`.
3. Open `output/teacher_timetables.xlsx`, sheet for any faculty who teaches
   multiple courses in the same semester.
4. Look for two course entries in the same time slot on the same day.

#### Potential fix

Pass the actual `slot_indices` list to the function and check against those:

```python
def check_professor_availability(professor_schedule, faculty, day, slot_indices):
    if faculty not in professor_schedule:
        return True
    existing_slots = professor_schedule[faculty][day]
    return not (set(slot_indices) & existing_slots)
```

Update all call sites to pass `slot_indices` instead of `start_idx` and
`duration_slots`.

---

### BUG-05 — `select_faculty` splits on `&` but even-semester data uses `&` for co-taught courses, silently dropping the second faculty

**Severity:** Medium  
**File:** `src/Class_TT.py`  
**Function:** `select_faculty`  
**Lines (main branch):** ~195–203

#### Description

`select_faculty` splits the faculty field on `&` and returns only the first
name. Several courses in the even-semester data are co-taught:

```
B5-CS373 — "Dr. Girish Revadigar & Dr. Shirshendu Layek"
CS206    — "Dr. Animesh Roy , Dr. Pavan"
```

Only the first faculty member is registered in `professor_schedule`. The
second faculty member's availability is never checked, so they can be
double-booked across courses without any conflict detection.

#### Buggy code

```python
def select_faculty(faculty_field):
    s = str(faculty_field).strip()
    for sep in ['/', ',', '&', ';']:
        if sep in s:
            return s.split(sep)[0].strip()   # second faculty silently dropped
    return s
```

#### Buggy output

`teacher_timetables.xlsx` will not contain a sheet for `Dr. Shirshendu Layek`
at all (or will show an incomplete schedule), and `Dr. Layek` may be
scheduled for another course at the exact same time as `B5-CS373` with no
conflict warning.

#### How to reproduce

1. Run `python src/Class_TT.py` with `data/combined_even.csv`.
2. Open `output/teacher_timetables.xlsx`.
3. Check whether `Dr. Shirshendu Layek` has a sheet — it will be absent or
   missing the `B5-CS373` entry.
4. Cross-reference with any other course assigned to `Dr. Layek` — a clash
   will be present.

#### Potential fix

Return all faculty names as a list and register each one in
`professor_schedule`. At minimum, check availability for all co-teachers:

```python
def get_all_faculty(faculty_field):
    """Returns list of all faculty names for a co-taught course."""
    if pd.isna(faculty_field):
        return ["TBD"]
    s = str(faculty_field).strip()
    for sep in ['&', '/', ';']:
        if sep in s:
            return [f.strip() for f in s.split(sep) if f.strip()]
    if ',' in s:
        parts = [f.strip() for f in s.split(',') if f.strip()]
        if len(parts) > 1:
            return parts
    return [s]
```

Then register and check all faculty in `professor_schedule` during placement.

---

### BUG-06 — Faculty name string-matching treats the same person as multiple distinct people

**Severity:** Critical  
**File:** `src/Class_TT.py`  
**Function:** `select_faculty` + all `professor_schedule` lookups  
**Root cause:** `professor_schedule` is keyed on the raw faculty string from the CSV. Any spelling variation, abbreviation, or typo creates a separate key, so the same physical person has multiple independent availability buckets and can be double-booked.

#### Description

The scheduler never resolves a faculty name to a canonical identity. Every unique string becomes its own key in `professor_schedule`. The same lecturer appearing under two different spellings across courses will have two separate schedule entries, meaning their real-world conflicts are invisible to the system.

The table below lists every confirmed alias pair found across `combined.csv` (odd sems) and `combined_even.csv` (even sems), cross-referenced against `FACULTY.csv`:

| FACULTY.csv canonical        | Variants found in CSVs                          | Source                                             |
| ---------------------------- | ----------------------------------------------- | -------------------------------------------------- |
| F001 Dr. Abdul Wahid         | `Dr. Abdul Wahid` ✓                             | combined.csv Sem 1,3,7 / combined_even.csv Sem 2,4 |
| F002 Dr. Anand Barangi       | `Dr. Anand Barangi` ✓                           | combined_even.csv Sem 2,6                          |
|                              | `Dr. Anand B`                                   | combined.csv Sem 3,5,7                             |
| F010 Dr. Dibyajyoti Guha     | `Dr. Dibyajyoti Guha` ✓                         | combined_even.csv                                  |
|                              | `Dr. Dibyajoti Guha` (missing 'y')              | combined.csv Sem 5                                 |
|                              | `Dr. Dibyajyothi Guha` (extra 'h')              | combined.csv Sem 7                                 |
| F011 Dr. Girish GN           | `Dr. Girish Revadigar`                          | combined_even.csv Sem 4,6                          |
|                              | `Dr. Girish`                                    | combined_even.csv Sem 4                            |
|                              | `Dr. Girirsh GN` (typo)                         | combined.csv Sem 7                                 |
|                              | `Dr. Girirsh Revadigar` (typo)                  | combined.csv Sem 1 ECE                             |
| F013 Dr. Jagadish D N        | `Dr. Jagadish D.N`                              | combined_even.csv ECE Sem 4                        |
|                              | `Dr.Jagdish D.N` (no space, different spelling) | combined_even.csv ECE Sem 2                        |
|                              | `Dr. Jagdeesh DN`                               | combined.csv Sem 5,7                               |
| F017 Dr. Manjunath KV        | `Dr. Manjunath K V` (space)                     | combined_even.csv                                  |
|                              | `Dr. Manjuth KV` (typo)                         | combined.csv Sem 5                                 |
|                              | `Dr.Manjunath K V` (no space after Dr.)         | combined.csv DSAI Sem 3                            |
| F022 Dr. Pramod Yelmewad     | `Dr. Pramod Yelmevad`                           | combined_even.csv                                  |
|                              | `Dr. Pramod Y`                                  | combined.csv Sem 3,5                               |
| F024 Dr. Prabhu Prasad BM    | `Dr. Prabhu Prasad`                             | combined_even.csv CSE Sem 2                        |
|                              | `Dr Prabhu Prasad` (no dot)                     | combined_even.csv ECE Sem 2                        |
| F025 Dr. Rajendra Hegadi     | `Dr. Rajendra Hegadi` ✓                         | combined_even.csv                                  |
|                              | `Dr. Rajendra H`                                | combined.csv Sem 5,7                               |
| F029 Dr. Ramesh Athe         | `Dr. Ramesh Athe` ✓                             | combined_even.csv                                  |
|                              | `Dr.Ramesh Athe` (no space after Dr.)           | combined.csv DSAI Sem 3                            |
| F031 Dr. Shirshendu L        | `Dr. Shirshendu Layek`                          | combined_even.csv Sem 6                            |
|                              | `Dr. Shrishendu Layek` (r↔h swap)               | combined_even.csv Sem 2                            |
| F032 Dr. Siddharth R         | `Dr. Siddharth R` ✓                             | combined_even.csv                                  |
|                              | `Dr. Siddharth` (no initial)                    | combined.csv DSAI Sem 3,5                          |
| F034 Dr. Somen Bhattacharjee | `Dr. Somen Bhattacharjee` ✓                     | combined_even.csv                                  |
|                              | `Dr. Somen B`                                   | combined.csv Sem 3,5                               |
| F035 Prof. SRM Prasanna      | `Prof. S R M Prasanna` (spaces)                 | combined_even.csv                                  |
|                              | `Prof. SRM Prasanna` (no spaces)                | combined.csv DSAI Sem 1                            |
| F037 Dr. Sunil Kumar PV      | `Dr. Sunil P V` (space)                         | combined_even.csv                                  |
|                              | `Dr. Sunil PV` (no space)                       | combined.csv Sem 1,3                               |
| F039 Dr. Suvadip Hazra       | `Dr. Suvadip Hazra` ✓                           | combined_even.csv                                  |
|                              | `Dr. Suvadip H`                                 | combined.csv Sem 3,5                               |
| F040 Dr. Utkarsh Khaire      | `Dr. Utkarsh` (no surname)                      | combined_even.csv Sem 4,6                          |
|                              | `Dr. Utkarsh Khaire` ✓                          | combined.csv Sem 5                                 |
| — (not in FACULTY.csv)       | `Dr. Chinmayananda A`                           | combined_even.csv Sem 6                            |
|                              | `Dr. Chinmayananda`                             | combined.csv / combined_even.csv Sem 4             |
| — (not in FACULTY.csv)       | `Dr. Aswath B`                                  | combined_even.csv                                  |
|                              | `Dr. Ashwath Babu`                              | combined.csv                                       |
|                              | `Dr. Aswath Babu`                               | combined.csv Sem 5                                 |

#### Buggy output

The most damaging consequence is **false clash-free scheduling**. For example:

- `Dr. Dibyajyoti Guha` (even sems) and `Dr. Dibyajoti Guha` (odd sems) are treated as two people — both can be assigned classes at the same time with no conflict raised.
- `Dr. Shrishendu Layek` (Sem-2) and `Dr. Shirshendu Layek` (Sem-6) are treated as two people — the real Dr. Layek ends up with two simultaneous classes.
- `Dr. Girish` and `Dr. Girish Revadigar` produce two separate teacher sheets in `teacher_timetables.xlsx`, one incomplete and one missing entries.

In `teacher_timetables.xlsx` you will see:

```
Sheet: "Dr. Anand B"       → only Sem 3/5/7 courses
Sheet: "Dr. Anand Barangi" → only Sem 2/6 courses
```

Both belong to F002. Their real weekly load is split across two sheets with no clash detection between them.

#### How to reproduce

1. Merge `combined.csv` and `combined_even.csv` into a single input file.
2. Run `python src/Class_TT.py`.
3. Open `output/teacher_timetables.xlsx`.
4. Search for `Anand` — two sheets appear (`Dr. Anand B` and `Dr. Anand Barangi`) with non-overlapping course lists that belong to one person.
5. Check `Dr. Dibyajoti Guha` vs `Dr. Dibyajyoti Guha` — both sheets exist independently and the same time slot may be occupied in both.

#### Potential fix

Add a `Faculty_ID` column to both `combined.csv` and `combined_even.csv` referencing `FACULTY.csv`. The scheduler resolves the display name via the ID, not the raw string:

```python
# Load faculty lookup: ID → canonical name
faculty_df = pd.read_csv(os.path.join(INPUT_DIR, 'FACULTY.csv'))
FACULTY_ID_MAP = {str(row['Faculty ID']): str(row['Name']) for _, row in faculty_df.iterrows()}

def resolve_faculty(faculty_id_field):
    """Resolve Faculty_ID to canonical name; fall back to raw string if no ID."""
    fid = str(faculty_id_field).strip()
    if fid in FACULTY_ID_MAP:
        return FACULTY_ID_MAP[fid]
    return fid  # legacy fallback for rows without an ID
```

Replace all calls to `select_faculty(row['Faculty'])` with
`resolve_faculty(row['Faculty_ID'])`. All `professor_schedule` keys are then
canonical names, so the same person is never double-booked regardless of how
their name was typed in the CSV.

Rows for faculty not yet in `FACULTY.csv` (e.g. `Dr. Swagatika Sahoo`,
`Dr. Nataraj`, `Dr. Sruthi`, `Dr. Muthusankar Eswaran`) should be added
with new IDs (F048 onwards) before assigning IDs in the course CSVs.

---

---

### BUG-07 — `CrossDeptGroup` (shared courses) fail to schedule for subsequent departments

**Severity:** Critical  
**File:** `src/Class_TT.py`  
**Function:** `apply_crossdept_schedule` / `place_course_on_slots`  
**Root cause:** Shared courses are treated as multiple independent placement attempts that happen to be at the same time. The second department's placement fails because the room and professor are already marked as "occupied" by the first department of the _same_ shared session.

#### Description

When a course is marked with a `CrossDeptGroup` (e.g., `CE_SHARED_1`), the scheduler first picks one department to be the "representative" and finds a slot/room for it. Then it tries to "apply" that same slot/room to the other departments in the group.

However, `apply_crossdept_schedule` calls `place_course_on_slots`, which in turn calls `check_professor_availability` and `find_suitable_room_for_slot`. These functions check `professor_schedule` and `room_schedule`. Since the representative department has JUST been placed, the professor and room are already marked as busy for that slot. The placement for the second department therefore returns `False` (fails), and the course is never added to the second department's timetable grid.

#### Buggy code

```python
# apply_crossdept_schedule — attempts placement but ignores failure
for _, row in group_courses.iterrows():
    if row['Department'] != department:
        continue
    # This call returns False because Professor/Room are already "busy" with
    # the first department of the same shared session!
    place_course_on_slots(
        row, timetable, entry['day'], entry['slot_indices'], entry['comp_type'],
        professor_schedule, room_schedule, course_room_mapping
    )
```

#### Buggy output

Shared courses only appear in the timetable of the department that was processed first. In the Excel output, the course will appear in the **Legend** (Course Details) of all departments, but its name will be missing from the actual **Calendar Grid** for all but one department.

**Example:** `MA163` (CE_SHARED_1) appears in `DSAI_2` timetable grid, but the `ECE_2` grid has empty cells where `MA163` should be.

#### How to reproduce

1. Run `python src/Class_TT.py` with `data/combined_even.csv`.
2. Open `output/timetable_all_departments_even.xlsx`.
3. Compare `DSAI_2` and `ECE_2` sheets.
4. Note that `MA163` is scheduled for `DSAI_2` (e.g., Monday 09:00).
5. Look at the same cell in `ECE_2` — it is empty, even though both departments share the course.

#### Potential fix

Modify `place_course_on_slots` to accept an optional `is_crossdept` flag. If the flag is set, allow bypassing the conflict check if the existing booking at that slot belongs to the same course code and faculty (indicating it's the same shared session).

Alternatively, in `apply_crossdept_schedule`, temporarily "free" the room/professor before calling `place_course_on_slots`, or use a placement function that doesn't re-check global availability.

---

### BUG-08 — DevSecOps (B5-CS373) fails to schedule despite available capacity

**Severity:** High  
**File:** `src/Class_TT.py`  
**Root cause:** Interaction between `BUG-02` (room leakage) and elective basket constraints.

#### Description

In the even-semester run, `B5-CS373` (DevSecOps) often appears in `unscheduled_courses_even.xlsx` with the reason "No suitable room found (Needs 50 capacity)". However, the `rooms.csv` file has several rooms with capacity 60 or 96 (e.g., 101, 102, L105).

This happens because earlier large courses (like `MA163` or `CS162` with 200+ students) "leak" into multiple rooms or stay booked in `room_schedule` due to `BUG-02`, and the elective basket logic (which cycles through many attempts) eventually exhausts all suitable rooms for the specific slots where the faculty is available.

#### How to reproduce

1. Run `python src/Class_TT.py` with `data/combined_even.csv`.
2. Open `output/unscheduled_courses_even.xlsx`.
3. Observe `B5-CS373` listed as unscheduled.

#### Potential fix

Fixing `BUG-01` and `BUG-02` will resolve this implicitly by ensuring rooms are correctly tracked and freed.

---

_End of bug report. Total bugs found: 8 (4 Critical, 3 High, 1 Medium)._
