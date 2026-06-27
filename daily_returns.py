import pandas as pd

# Load cleaned NAV history
df = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by scheme and date
df = df.sort_values(
    ["amfi_code", "date"]
)

# Calculate daily return
df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
      .pct_change()
)

# Display first 10 rows
print(df.head(10))

# Summary statistics
print("\nDaily Return Summary")
print(df["daily_return"].describe())

# Highest daily returns
print("\nTop 5 Highest Daily Returns")
print(df["daily_return"].nlargest(5))

# Lowest daily returns
print("\nTop 5 Lowest Daily Returns")
print(df["daily_return"].nsmallest(5))

# Save output
df.to_csv(
    "data/processed/nav_daily_returns.csv",
    index=False
)

print("\nDaily returns calculated successfully!")