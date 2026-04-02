import subprocess
import os

TESTS = [
    "TC-NEW-01", "TC-NEW-02", "TC-NEW-03", "TC-NEW-04",
    "TC-SMART-01", "TC-SMART-02", "TC-SMART-03", "TC-SMART-04", "TC-SMART-05"
]

def run_all():
    results = {}
    for tc in TESTS:
        print(f"--- RUNNING {tc} ---")
        cmd = ["python", "tests/run_test.py", "--tc", tc]
        res = subprocess.run(cmd, capture_output=True, text=True)
        print(res.stdout)
        
        # Parse summary from stdout
        summary_line = [l for l in res.stdout.split('\n') if "SUMMARY" in l]
        if summary_line:
            results[tc] = summary_line[0]
        else:
            # Fallback for old output format
            failed_line = [l for l in res.stdout.split('\n') if "FAILED" in l]
            if failed_line:
                results[tc] = failed_line[0]
            else:
                results[tc] = "No summary found"
                
    print("\n\n=== FINAL RESULTS SUMMARY ===")
    for tc, res in results.items():
        print(f"{tc}: {res}")

if __name__ == "__main__":
    run_all()
