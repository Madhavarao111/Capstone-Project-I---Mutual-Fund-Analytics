import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/raw/Bluestock_MF_Datasets/08_investor_transactions.csv"
)

print("Original Shape:", df.shape)

# Convert date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Validate amount > 0
df = df[df["amount_inr"] > 0]

# Standardize KYC status
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.title()
)

# Check valid KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Remove duplicates
df = df.drop_duplicates()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)
print("Transactions Cleaned Successfully!")