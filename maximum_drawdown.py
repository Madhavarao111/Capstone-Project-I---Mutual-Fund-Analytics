import pandas as pd

# Load NAV history
df = pd.read_csv("data/processed/nav_daily_returns.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by fund and date
df = df.sort_values(["amfi_code", "date"])

results = []

# Process each mutual fund
for code, group in df.groupby("amfi_code"):

    # Sort records by date and reset index
    group = group.sort_values("date").reset_index(drop=True)

    # Calculate running maximum NAV
    group["running_max"] = group["nav"].cummax()

    # Calculate drawdown
    group["drawdown"] = (
    group["nav"] / group["running_max"]) - 1

    # Find maximum drawdown
    max_drawdown = group["drawdown"].min()

    # Find the row where maximum drawdown occurred
    worst_index = group["drawdown"].idxmin()
    worst_row = group.loc[worst_index]

    # Find the peak before the drawdown
    peak_index = group.loc[:worst_index, "nav"].idxmax()
    peak_row = group.loc[peak_index]

    # Store results
    results.append({
        "amfi_code": code,
        "Peak_Date": peak_row["date"].date(),
        "Trough_Date": worst_row["date"].date(),
        "Maximum_Drawdown (%)": round(max_drawdown * 100,2)
    })

# Create DataFrame
mdd_df = pd.DataFrame(results)

# Rank funds (least negative drawdown is better)
mdd_df = mdd_df.sort_values("Maximum_Drawdown (%)",ascending=False)

mdd_df["Rank"] = range(1,len(mdd_df) + 1)

# Display results
print("\nMaximum Drawdown Results")
print(mdd_df)

# Save results
mdd_df.to_csv("data/processed/maximum_drawdown.csv",index=False)

print("\nMaximum Drawdown calculation completed successfully!")