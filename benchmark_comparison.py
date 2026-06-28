import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load fund scorecard
scorecard = pd.read_csv("data/processed/fund_scorecard.csv")

# Load fund NAV history
fund_df = pd.read_csv("data/processed/nav_daily_returns.csv")

# Load benchmark data
benchmark_df = pd.read_csv("data/raw/Bluestock_MF_Datasets/10_benchmark_indices.csv")

# Convert date columns
fund_df["date"] = pd.to_datetime(fund_df["date"])

benchmark_df["date"] = pd.to_datetime(benchmark_df["date"])

# Select Top 5 funds
top5 = scorecard.nsmallest(5,"Overall_Rank")

top5_codes = top5["amfi_code"].tolist()

print("\nTop 5 Funds")
print(
    top5[
        [
            "Overall_Rank",
            "amfi_code",
            "scheme_name"
        ]
    ]
)

# Keep only Top 5 funds
fund_df = fund_df[
    fund_df["amfi_code"].isin(top5_codes)
]

# Keep only NIFTY50 and NIFTY100
benchmark_df = benchmark_df[
    benchmark_df["index_name"].isin(
        [
            "NIFTY50",
            "NIFTY100"
        ]
    )
]

# Sort benchmark
benchmark_df = benchmark_df.sort_values(
    [
        "index_name",
        "date"
    ]
)

# Calculate benchmark daily returns
benchmark_df["benchmark_return"] = (
    benchmark_df.groupby("index_name")[
        "close_value"
    ].pct_change()
)

tracking_results = []

# Calculate Tracking Error
for code in top5_codes:

    fund = fund_df[
        fund_df["amfi_code"] == code
    ]

    for benchmark in [
        "NIFTY50",
        "NIFTY100"
    ]:

        bench = benchmark_df[
            benchmark_df["index_name"] == benchmark
        ]

        merged = pd.merge(
            fund,
            bench,
            on="date",
            how="inner"
        )

        merged = merged.dropna(
            subset=[
                "daily_return",
                "benchmark_return"
            ]
        )

        tracking_error = (
            (
                merged["daily_return"]
                -
                merged["benchmark_return"]
            ).std()
        ) * np.sqrt(252)

        tracking_results.append(
            {
                "amfi_code": code,
                "Benchmark": benchmark,
                "Tracking_Error":
                round(
                    tracking_error,
                    4
                )
            }
        )

# Create Tracking Error DataFrame
tracking_df = pd.DataFrame(
    tracking_results
)

print("\nTracking Error")
print(tracking_df)

# Save Tracking Error
tracking_df.to_csv(
    "data/processed/tracking_error.csv",
    index=False
)

# -----------------------------
# Benchmark Comparison Chart
# -----------------------------

plt.figure(figsize=(14,7))

# Plot Top 5 Funds (Normalized NAV)
for code in top5_codes:

    temp = fund_df[
        fund_df["amfi_code"] == code
    ].sort_values("date")

    temp["normalized_nav"] = (
        temp["nav"]
        /
        temp["nav"].iloc[0]
    ) * 100

    scheme = scorecard.loc[
        scorecard["amfi_code"] == code,
        "scheme_name"
    ].values[0]

    plt.plot(
        temp["date"],
        temp["normalized_nav"],
        label=scheme
    )

# Plot Benchmarks (Normalized)

for benchmark in [
    "NIFTY50",
    "NIFTY100"
]:

    temp = benchmark_df[
        benchmark_df["index_name"] == benchmark
    ].sort_values("date")

    temp["normalized_index"] = (
        temp["close_value"]
        /
        temp["close_value"].iloc[0]
    ) * 100

    plt.plot(
        temp["date"],
        temp["normalized_index"],
        linewidth=2.5,
        linestyle="--",
        label=benchmark
    )

# Chart Labels

plt.title(
    "Top 5 Funds vs NIFTY50 & NIFTY100 (3 Years)"
)

plt.xlabel("Date")

plt.ylabel(
    "Normalized Value (Base = 100)"
)

plt.legend()

plt.grid(True)

plt.tight_layout()

# Save Chart
plt.savefig(
    "data/processed/benchmark_comparison.png",
    dpi=300
)

plt.show()

print(
    "\nBenchmark comparison completed successfully!"
)