import pandas as pd
import numpy as np

# Load daily returns dataset
df = pd.read_csv("data/processed/nav_daily_returns.csv")

# Risk-Free Rate (Annual)
risk_free_rate = 0.065

# Convert annual rate to daily rate
daily_rf = risk_free_rate / 252

# Store Sortino Ratio results
results = []

# Process each mutual fund separately
for code, group in df.groupby('amfi_code'):

    #Remove missing daily returns
    returns = group["daily_return"].dropna()

    # Skip if there are no returns
    if returns.empty:
        continue

    # Average daily return
    avg_return = returns.mean()

    # Select only negative return days
    downside_returns = returns[returns < 0]

    # Calculate downside standard deviation
    downside_std = downside_returns.std()

    # Avoid division by zero or NaN
    if pd.isna(downside_std) or downside_std == 0:
        sortino = None
    else:
        # Sortino Ratio Formula
        sortino = ((avg_return - daily_rf)/ downside_std) * np.sqrt(252)

    #Store results
    results.append({
        "amfi_code": code,
        "Average_Return": round(avg_return * 100, 4),
        "Downside_Std": round(downside_std * 100, 4) if pd.notna(downside_std) else None,
        "Sortino_Ratio": round(sortino, 4) 
        if sortino is not None else None
    })

# Create DataFrame from results
sortino_df = pd.DataFrame(results)

# Rank Funds by Sortino Ratio
sortino_df = sortino_df.sort_values("Sortino_Ratio", ascending=False)
sortino_df["Rank"] = range(1, len(sortino_df) + 1)

# Display results
print("\nSortino Ratio Ranking")
print(sortino_df)

# Save results to CSV
sortino_df.to_csv("data/processed/sortino_ratio.csv", index=False)

print("\nSortino Ratio calculation completed successfully")
