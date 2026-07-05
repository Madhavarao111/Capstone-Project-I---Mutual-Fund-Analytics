import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

scripts = [
    "daily_returns.py",
    "cagr_calculation.py",
    "sharpe_ratio.py",
    "sortino_ratio.py",
    "alpha_beta.py",
    "maximum_drawdown.py",
    "fund_scorecard.py",
    "benchmark_comparison.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run(
        ["python", str(BASE_DIR / script)],
        check=True
    )

print("\nAll Performance Metrics Completed Successfully!")