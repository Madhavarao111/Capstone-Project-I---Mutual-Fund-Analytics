import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/raw/Bluestock_MF_Datasets/01_fund_master.csv"
)

print("=" * 70)
print("FUND MASTER ANALYSIS")
print("=" * 70)

# Dataset info
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# Fund Houses
print("\n" + "=" * 70)
print("FUND HOUSES")
print("=" * 70)
print(df["fund_house"].unique())
print(f"\nTotal Fund Houses: {df['fund_house'].nunique()}")

# Categories
print("\n" + "=" * 70)
print("CATEGORIES")
print("=" * 70)
print(df["category"].unique())
print(f"\nTotal Categories: {df['category'].nunique()}")

# Sub Categories
print("\n" + "=" * 70)
print("SUB CATEGORIES")
print("=" * 70)
print(df["sub_category"].unique())
print(f"\nTotal Sub Categories: {df['sub_category'].nunique()}")

# Risk Category (if column exists)
print("\n" + "=" * 70)
print("RISK CATEGORIES")
print("=" * 70)

if "risk_category" in df.columns:
    print(df["risk_category"].unique())
    print(f"\nTotal Risk Categories: {df['risk_category'].nunique()}")
else:
    print("risk_category column not found.")

# Missing values
print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)
print(df.isnull().sum())

# Duplicate rows
print("\n" + "=" * 70)
print("DUPLICATE ROWS")
print("=" * 70)
print(df.duplicated().sum())

print("\nAnalysis Complete!")