import os
import shutil
import subprocess
import argparse
import pandas as pd

PROJECT_ROOT = os.getcwd()
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
TESTS_DIR = os.path.join(PROJECT_ROOT, 'tests')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')

def setup_test_case(tc_id):
    tc_path = os.path.join(TESTS_DIR, tc_id)
    if not os.path.exists(tc_path):
        # Check legacy folder
        tc_path = os.path.join(TESTS_DIR, 'legacy', tc_id)
    
    tc_data_path = os.path.join(tc_path, 'data')
    
    if not os.path.exists(tc_data_path):
        print(f"Error: Test case {tc_id} data not found at {tc_data_path}")
        return False
    
    # 1. Clear current data/
    print(f"Cleaning {DATA_DIR}...")
    for f in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, f)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"  Warning: Failed to remove {f}: {e}")
            
    # 2. Clear output/ to avoid stale results leaking
    print(f"Cleaning {OUTPUT_DIR}...")
    if os.path.exists(OUTPUT_DIR):
        for f in os.listdir(OUTPUT_DIR):
            file_path = os.path.join(OUTPUT_DIR, f)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"  Warning: Failed to clear output file {f}: {e}")
    else:
        os.makedirs(OUTPUT_DIR)

    # 3. Copy TC data to data/
    print(f"Copying data from {tc_data_path} to {DATA_DIR}...")
    for f in os.listdir(tc_data_path):
        src = os.path.join(tc_data_path, f)
        dst = os.path.join(DATA_DIR, f)
        shutil.copy(src, dst)
        print(f"  Copied {f}")
        
    print(f"Setup complete for {tc_id}")
    return True

def run_scheduler():
    script_path = os.path.join(PROJECT_ROOT, 'src', 'Class_TT.py')
    print(f"Running scheduler: {script_path}")
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    return result

def save_results(tc_id):
    tc_path = os.path.join(TESTS_DIR, tc_id)
    if not os.path.exists(tc_path):
        tc_path = os.path.join(TESTS_DIR, 'legacy', tc_id)
        
    tc_output_path = os.path.join(tc_path, 'results')
    if os.path.exists(tc_output_path):
        shutil.rmtree(tc_output_path)
    os.makedirs(tc_output_path)
    
    essential_files = [
        'timetable_all_departments_even.xlsx',
        'teacher_timetables_even.xlsx',
        'unscheduled_courses_even.xlsx'
    ]
    
    if os.path.exists(OUTPUT_DIR):
        for f in os.listdir(OUTPUT_DIR):
            if f in essential_files or f.endswith('.log'):
                shutil.copy(os.path.join(OUTPUT_DIR, f), os.path.join(tc_output_path, f))
                print(f"  Saved result: {f}")
    
    print(f"Results saved for {tc_id} to {tc_output_path}")

def main():
    parser = argparse.ArgumentParser(description='Run a specific test case for the scheduler.')
    parser.add_argument('--tc', type=str, required=True, help='Test case ID (e.g., TC-01)')
    args = parser.parse_args()
    
    tc_id = args.tc
    if setup_test_case(tc_id):
        result = run_scheduler()
        print(result.stdout)
        if result.stderr:
            print("Errors/Warnings:")
            print(result.stderr)
        save_results(tc_id)
        
        unscheduled_file = os.path.join(OUTPUT_DIR, 'unscheduled_courses_even.xlsx')
        if os.path.exists(unscheduled_file):
            try:
                df = pd.read_excel(unscheduled_file)
                print(f"SUMMARY: {len(df)} components unscheduled.")
            except Exception as e:
                print(f"Error reading results: {e}")
        else:
            print("SUMMARY: 0 components unscheduled (Pass).")

if __name__ == "__main__":
    main()
