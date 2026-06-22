import pandas as pd

fund_master = pd.read_csv(
    "data/raw/Bluestock_MF_Datasets/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/Bluestock_MF_Datasets/02_nav_history.csv"
)

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing = master_codes - nav_codes

print("Missing Codes:", missing)
print("Count:", len(missing))