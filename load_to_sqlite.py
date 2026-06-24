from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

fund = pd.read_csv(
    "data/raw/Bluestock_MF_Datasets/01_fund_master.csv"
)

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded Successfully")