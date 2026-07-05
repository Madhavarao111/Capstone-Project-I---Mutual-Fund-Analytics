import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

scripts = [
    "clean_nav_history.py",
    "clean_transactions.py",
    "clean_scheme_performance.py",
    "load_to_sqlite.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run(
        ["python", str(BASE_DIR / script)],
        check=True
    )

print("\nETL Pipeline Completed Successfully!")