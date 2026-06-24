import pandas as pd

df = pd.read_csv(
    "data/raw/Bluestock_MF_Datasets/07_scheme_performance.csv"
)

# Return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

# Convert returns to numeric
for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Find anomalies
anomalies = df[
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100)
]

print("\nAnomalies Found:")
print(anomalies)

# Check expense ratio range
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratios:")
print(invalid_expense)

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("\nCleaning Complete!")