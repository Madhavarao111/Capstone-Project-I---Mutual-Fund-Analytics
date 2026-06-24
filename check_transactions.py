import pandas as pd

df = pd.read_csv(
    "data/raw/Bluestock_MF_Datasets/08_investor_transactions.csv"
)

print(df.columns.tolist())
print(df.head())