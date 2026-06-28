import pandas as pd
from scipy.stats import linregress

#load cleaned NAV history with daily returns
fund_df = pd.read_csv("data/processed/nav_daily_returns.csv")

#load benchmark index data
benchmark_df = pd.read_csv("data/raw/Bluestock_MF_Datasets/10_benchmark_indices.csv")

#convert date columns to datetime
fund_df["date"] = pd.to_datetime(fund_df["date"])
benchmark_df["date"] = pd.to_datetime(benchmark_df["date"])

#filter benchmark for NIFTY100 index
benchmark_df = benchmark_df[benchmark_df["index_name"] == "NIFTY100"]

#sort by date
benchmark_df = benchmark_df.sort_values("date")

#calculate daily returns for benchmark
benchmark_df["benchmark_return"] = (benchmark_df["close_value"].pct_change())

#keep only relevant columns
benchmark_df = benchmark_df[["date", "benchmark_return"]]

#store alpha and beta results
results = []

#process each fund separately
for code, group in fund_df.groupby("amfi_code"):

    # Merge fund returns with benchmark returns
    merged = pd.merge(group,benchmark_df,on="date",how="inner")

    # Remove missing values
    merged = merged.dropna(subset=["daily_return", "benchmark_return"])

    # Skip if insufficient data
    if len(merged) < 2:
        continue

    # Linear Regression
    # X = Benchmark Returns
    # Y = Fund Returns
    slope, intercept, r_value, p_value, std_err = linregress(merged["benchmark_return"],merged["daily_return"])

    # Beta = slope
    beta = slope

    # Alpha = intercept × 252
    alpha = intercept * 252

    # Save results
    results.append({
        "amfi_code": code,
        "Alpha": round(alpha, 4),
        "Beta": round(beta, 4),
        "R_Squared": round(r_value ** 2, 4)
    })

# Create DataFrame from results
alpha_beta_df = pd.DataFrame(results)


# Rank by Alpha
alpha_beta_df = alpha_beta_df.sort_values("Alpha",ascending=False)

alpha_beta_df["Rank"] = range(1,len(alpha_beta_df) + 1)

#Display results
print("\nAlpha & Beta Results")
print(alpha_beta_df)

# Save CSV
alpha_beta_df.to_csv(
    "data/processed/alpha_beta.csv",
    index=False
)

print("\nAlpha & Beta calculation completed successfully!")