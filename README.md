# Automated Time-Table Scheduling at IIIT Dharwad

Generate clash-free class timetables (lectures, tutorials, labs, and elective baskets) using course, room, and faculty data. The output is an Excel workbook for each section plus teacher schedules and a list of unscheduled courses.

**What this tool does**

- Schedules lectures, tutorials, and labs with faculty and room constraints
- Supports elective baskets and shared cross-department courses
- Enforces room capacity and lab/lecture room types
- Produces color-coded Excel timetables, teacher timetables, and an unscheduled list

## Quick Start

**Requirements**

- Python 3.10+ (3.11+ recommended)
- Windows/macOS/Linux

**Install**

```bash
git clone <your-repo-url>
cd Automated-Time-Table-Scheduling-At-IIIT-Dharwad
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

**Run**

```bash
python src/Class_TT.py
```

Outputs are written to `output/`:

- `timetable_all_departments.xlsx`
- `teacher_timetables.xlsx`
- `unscheduled_courses.xlsx`

## Data Inputs

All inputs live in `data/`:

- `combined.csv`
  Course list with L/T/P values, faculty, semester, and student counts.
- `rooms.csv`
  Room number, room type (e.g., `LECTURE_ROOM`, `COMPUTER_LAB`), and capacity.
- `config.json`
  Scheduling settings (days, slot durations, etc.).

## Configuration

Edit `data/config.json` to tune the scheduler. Example keys:

- `days` (list of weekdays)
- `LECTURE_MIN`, `TUTORIAL_MIN`, `LAB_MIN` (slot duration in minutes)
- `SELF_STUDY_MIN` (if used)

## Project Structure

```
Automated-Time-Table-Scheduling-At-IIIT-Dharwad/
|-- README.md
|-- requirements.txt
|-- src/
|   |-- Class_TT.py
|-- data/
|   |-- combined.csv
|   |-- rooms.csv
|   |-- config.json
|-- tests/
|   |-- run_test.py             # Single test runner
|   |-- run_all_sequentially.py  # Full suite runner
|   |-- TC-NEW-01/              # Stress Test: Room Starvation
|   |-- TC-SMART-03/            # Smart Test: Student Starvation
|   |-- ...                     # Other test scenarios
|-- output/
```

## 🧪 Testing Infrastructure (Stress & Smart Tests)

This repository includes a specialized testing suite designed to identify system failure modes and validate constraints.

### Running a Specific Test

To run a single test case (e.g., TC-NEW-01):

```bash
python tests/run_test.py --tc TC-NEW-01
```

This will:

1. Clear the current `data/` and `output/` folders.
2. Load the specific scenario's input data.
3. Run the scheduler and isolate the results in `tests/TC-NEW-01/results/`.

### Running All Tests

To execute all 9 stress and smart tests sequentially:

```bash
python tests/run_all_sequentially.py
```

### Test Categories

- **Stress Tests (TC-NEW-01 to 04)**: Resource starvation, faculty overload, high student strength, and peak load.
- **Smart Tests (TC-SMART-01 to 05)**: Advanced logic checks like "Student Time Starvation" and "Cross-Departmental Synchronization".
- **Legacy Tests (TC-01 to 15)**: Basic functionality checks (moved to legacy).

### Test Outputs

Each test produces exactly 3 essential files in its `results/` folder:

- `unscheduled_courses_even.xlsx`: Detailed failure reasons.
- `timetable_all_departments_even.xlsx`: The generated departmental schedule.
- `teacher_timetables_even.xlsx`: Faculty-specific schedules.

## 🧪 Test Case Inventory

The following 20 test scenarios are used to validate the scheduler's performance and constraint enforcement:

| ID        | Category | Focus / Scenario                                                                          |
| :-------- | :------- | :---------------------------------------------------------------------------------------- |
| **TC-01** | Stress   | **Room Starvation**: Deliberately starves the system of classrooms.                       |
| **TC-02** | Stress   | **Faculty Starvation**: Multiple courses assigned to the same unassigned "TBD" faculty.   |
| **TC-03** | Stress   | **Student Starvation**: Total students in a section exceed all available room capacities. |
| **TC-04** | Stress   | **Peak Load**: Maximizes sessions per day to test slot availability.                      |
| **TC-05** | Logic    | **Basic CSE**: Validates standard Semester 4 scheduling.                                  |
| **TC-06** | Logic    | **Basic ECE**: Validates standard Semester 6 scheduling.                                  |
| **TC-07** | Logic    | **Basic DSAI**: Validates standard Semester 2 scheduling.                                 |
| **TC-08** | Logic    | **Multiple Baskets**: Multiple elective baskets in a single semester.                     |
| **TC-09** | Logic    | **Shared Faculty**: Single faculty member teaching across multiple departments.           |
| **TC-10** | Logic    | **Large Hall**: Validates auto-allocation of C004 for 120+ students.                      |
| **TC-11** | Stress   | **Lab Starvation**: Deliberately restricts Computer Lab availability.                     |
| **TC-12** | Logic    | **Session Stacking**: Multiple Tut/Labs on the same day.                                  |
| **TC-13** | Stress   | **High Capacity**: Multiple courses requiring >120 capacity rooms.                        |
| **TC-14** | Logic    | **Semester 1 (Odd)**: Basic odd semester scheduling.                                      |
| **TC-15** | Logic    | **Semester 5 (Odd)**: Advanced odd semester scheduling.                                   |
| **TC-16** | Feature  | **Multi-Department**: Simultaneous CSE + ECE generation.                                  |
| **TC-17** | Feature  | **Multi-Section**: Simultaneous CSE Section A + Section B.                                |
| **TC-18** | Feature  | **Shared Courses**: Validates `CE_SHARED` room and strength synchronization.              |
| **TC-19** | Feature  | **Full Institute (Even)**: All departments, all even semesters.                           |
| **TC-20** | Feature  | **Full Institute (Odd)**: All departments, all odd semesters.                             |

## 🐞 Known Logic Failures (To be fixed in `devM`)

The following critical bugs were identified during testing:

1.  **Bug #2 (Faculty Collision):** All unassigned faculty default to a generic "TBD" string. The scheduler treats them as a single person, preventing multiple "TBD" courses from being scheduled at the same time.
2.  **Bug #3 (CE_SHARED Synchronization):** Cross-department shared courses fail to communicate. They may be assigned to different rooms by different departments and fail to aggregate total student strength for capacity checks.
3.  **Bug #4 (Room Overlap & Phantom Bookings):** Elective baskets can double-book rooms during the same time slot. Additionally, unscheduled courses may incorrectly appear in reports with "Room: None".

These issues are resolved in the **`devM`** branch.
