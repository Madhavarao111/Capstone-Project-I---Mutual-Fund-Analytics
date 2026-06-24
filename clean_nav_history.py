import pandas as pd

df = pd.read_csv(
    "data/raw/Bluestock_MF_Datasets/02_nav_history.csv"
)

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(
    by=["amfi_code", "date"]
)

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

df = df.drop_duplicates()

df = df[df["nav"] > 0]

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print(df.shape)
print("NAV History Cleaned Successfully!")