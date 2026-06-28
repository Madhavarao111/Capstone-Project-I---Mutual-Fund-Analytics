import pandas as pd
import numpy as np

# Load cleaned NAV history
df = pd.read_csv("data/processed/nav_daily_returns.csv")

# Annual Risk-Free Rate (RBI Repo Proxy)
risk_free_rate = 0.065

# Convert annual rate to daily rate
daily_rf = risk_free_rate / 252

# Store Sharpe Ratio results
results = []

# calulate Sharpe Ratio for each fund
for code,group in df.groupby('amfi_code'):

    # Remove missing daily returns
    returns = group["daily_return"].dropna()

    # Skip if no returns exist
    if len(returns) == 0:
        continue

    #average daily return
    avg_return = returns.mean()

    #standard deviation of daily returns
    std_return = returns.std()

    # Avoid division by zero
    if std_return == 0:
        sharpe = None
    else:
        sharpe = ((avg_return - daily_rf)/ std_return) * np.sqrt(252)

    results.append({"amfi_code": code, 
                    "Average_Return": round(avg_return * 100, 4),
                    "Std_Deviation": round(std_return * 100, 4),
                    "Sharpe_Ratio": round(sharpe, 4)})
    
# Create DataFrame for results
sharpe_df = pd.DataFrame(results)

#Rank Funds
sharpe_df = sharpe_df.sort_values("Sharpe_Ratio", ascending=False)
sharpe_df["Rank"] = range(1, len(sharpe_df) + 1)

# Dsplay results
print("\nSharpe Ratio Ranking")
print(sharpe_df)

# Save output
sharpe_df.to_csv("data/processed/sharpe_ratio.csv", index=False)

print("\nSharpe Ratio calculation completed successfully!")

