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

## Troubleshooting

- `combined.csv` not found: Ensure `data/combined.csv` exists.
- Rooms not loading: Check `data/rooms.csv` headers and values.
- Many unscheduled courses:
  - Add more rooms or increase room capacities.
  - Relax constraints in `data/config.json`.
  - Extend the available time slots.
