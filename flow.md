# Timetable Generator — Code Flow Documentation

## Lines 1–110: Setup & Config
* **Imports:** `pandas`, `openpyxl`, `json`, etc.
* **Loads `config.json`:**
    * `LECTURE_MIN` = 90
    * `LAB_MIN` = 120
    * `TUTORIAL_MIN` = 60
    * Working days definition.
* **Defines paths:** `data/`, `output/`
* **Loads Data:**
    * `combined_even.csv` (course list)
    * `rooms.csv` (infrastructure)
* **Builds `ROOM_DATA` dictionary:**
    * Key: Room number
    * Values: Type, Capacity

---

## Lines 111–300: Time Slots & Core Helpers

### Time Slot Generation
* **`generate_time_slots()`**
    * Creates slots from **7:30 AM → 8:00 PM**
    * Includes lunch break: **13:15–14:00**
    * Total: **20 slots/day**

### Helper Functions
* **`slot_minutes()`**: Returns slot duration.
* **`overlaps()`**: Checks for time conflicts.
* **`is_break_time_slot()`**: Blocks lunch scheduling.
* **`is_minor_slot()`**: Avoids early/late slots for specific components.

### Course/Faculty Logic
* **`select_faculty()`**: Picks the first faculty from the list.
* **`get_course_priority()`**: Sorts by L+T+P weight.
* **`calculate_required_minutes()`**: Computes required duration for scheduling.

### Lecture Planning
* **`get_lecture_session_plans()`**
    * Splits lectures into: 1 × 120 min OR 2 × 60 min sessions.

---

## Lines 300–540: Room Allocation & Slot Finding

### Room Selection
* **`find_suitable_room_for_slot()`**
    * **Priority:**
        1. Forced room (e.g., `-C004` suffix).
        2. Previously assigned room for continuity.
        3. Best-fit room: Correct type, Capacity ≥ students, Smallest possible.
        4. Fallback: Combine two labs if needed.

### Slot Finding
* **`find_consecutive_slots_for_minutes()`**
    * Walks forward through the grid accumulating minutes.
    * **Constraints:**
        * No LEC + TUT on the same day.
        * No multiple LECs per day.
        * No back-to-back lectures.
        * Faculty availability check.

### Faculty Check
* **`check_professor_availability()`**
    * Uses set intersection to ensure the professor isn't booked elsewhere.

---

## Lines 540–900: Scheduling Primitives

### Core Placement
* **`place_course_on_slots()`**
    * Writes: Course info, Faculty, Room.
    * Updates: `professor_schedule`, `room_schedule`.

### Special Scheduling
* **Cross-Department Courses (`schedule_crossdept_group`)**: Scheduled once and mirrored across involved departments.
* **Combined Sections (CSE A/B)**: `schedule_combined_courses()` schedules once, then `apply_combined_schedule()` copies it to the twin section.
* **Basket Enforcement**: `enforce_basket_slots()` locks predefined elective slots.

---

## Lines 893–1260: Global Elective Basket Scheduling

### `schedule_global_elective_baskets()`
* Runs **before all other scheduling**.
* Assigns slots for `(semester, basket)` pairs.
* **Rules:**
    * Prevent conflicts within the same basket.
    * Allow overlap across different baskets.
    * Avoid consecutive LEC/LAB across different baskets.
* **Strategy:** Random slot selection with up to **5,000 retry attempts** before relaxing constraints.
* **Output:** `global_schedule[(semester, basket)] = [(day, slot_indices, component_type)]`

---

## Lines 1278–1720: Main Orchestration

### `generate_all_timetables()`

1.  **Preprocessing:** Call `schedule_global_elective_baskets()`, create Excel workbook, add Overview sheet.
2.  **Section Loop:** Iterates over (Department, Semester). CSE handles Sections A & B; others handle single sections.
3.  **Per Section Logic:**
    * Create empty timetable grid.
    * Apply locked basket slots.
    * Schedule: Combined courses → Cross-dept courses → Regular courses (random placement).
4.  **Output:** Call `write_timetable_to_sheet()`.
5.  **Special Case:** 7th semester is handled via its own logic.
6.  **Final Steps:** Save workbook and trigger Teacher/Unscheduled reports.

---

## Lines 1725–2050: 7th Semester Common Timetable

### `generate_7th_sem_common_timetable()`
* Combines CSE, DSAI, and ECE.
* **Electives:** Grouped by basket; scheduled at the same time but in different rooms.
* **Non-electives:** Scheduled individually.

---

## Lines 2052–2360: Excel Rendering

### `write_timetable_to_sheet()`
* **Layout:** Row 1 (Time slots), Rows 2–6 (Days Mon–Fri).
* **Features:**
    * Color coding (Pastels per course; distinct colors for LEC/LAB/TUT).
    * Merge consecutive cells for long sessions.
    * Course Details legend at the bottom.
    * Metadata stored in hidden `_META` sheet.

---

## Lines 2361–2497: Overview Sheet

### `format_overview_sheet()`
* **Styling:** Merged headers, alternating row colors, auto-filters, freeze panes, and blue tab color for navigation.

---

## Lines 2497–End: Teacher Timetables & Reports

### `create_teacher_and_unscheduled_from_combined()`

* **Teacher Timetables:**
    * Parses generated Excel cells.
    * Extracts faculty names using `_META` sheet.
    * Builds `teacher_slots` and exports to `teacher_timetables_even.xlsx`.
* **Unscheduled Courses:**
    * Compares the master course list against scheduled entries.
    * Generates `unscheduled_courses_even.xlsx` with specific failure reasons.

---

## Overall Flow Summary
1.  **Load Data** (Config, CSVs, Rooms)
2.  **Global Basket Scheduling** (Pre-lock elective slots)
3.  **Per Section Scheduling** (Baskets → Combined → Cross-dept → Regular)
4.  **Write Timetable to Excel** (Formatting, Merging, Coloring)
5.  **Generate Teacher Timetables** (Extraction from Section sheets)
6.  **Generate Unscheduled Report** (Audit/Error logging)
