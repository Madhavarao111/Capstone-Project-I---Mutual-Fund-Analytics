from pathlib import Path
from sqlalchemy import create_engine, text
import pandas as pd

# ==========================================
# Project Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw" / "Bluestock_MF_Datasets"

PROCESSED_DIR = DATA_DIR / "processed"

DB_DIR = DATA_DIR / "db"
DB_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_DIR / "bluestock_mf.db"

# ==========================================
# Create SQLite Connection
# ==========================================

engine = create_engine(f"sqlite:///{DB_PATH}")

# ==========================================
# Read CSV Files
# ==========================================

print("Loading CSV files...\n")

fund = pd.read_csv(
    RAW_DIR / "01_fund_master.csv"
)

nav = pd.read_csv(
    PROCESSED_DIR / "nav_history_clean.csv"
)

transactions = pd.read_csv(
    PROCESSED_DIR / "investor_transactions_clean.csv"
)

performance = pd.read_csv(
    PROCESSED_DIR / "scheme_performance_clean.csv"
)

aum = pd.read_csv(
    RAW_DIR / "03_aum_by_fund_house.csv"
)

# ==========================================
# Load Data into SQLite
# ==========================================

print("Loading data into SQLite...\n")

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("All datasets loaded successfully!")

# ==========================================
# Verify CSV Row Counts
# ==========================================

print("\nCSV Row Counts")
print("-" * 35)

print(f"dim_fund          : {len(fund)}")
print(f"fact_nav          : {len(nav)}")
print(f"fact_transactions : {len(transactions)}")
print(f"fact_performance  : {len(performance)}")
print(f"fact_aum          : {len(aum)}")

# ==========================================
# Verify Database Row Counts
# ==========================================

print("\nDatabase Row Counts")
print("-" * 35)

with engine.connect() as conn:

    tables = [
        "dim_fund",
        "fact_nav",
        "fact_transactions",
        "fact_performance",
        "fact_aum"
    ]

    for table in tables:

        count = conn.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        ).scalar()

        print(f"{table:<18}: {count}")

# ==========================================
# Show Database Information
# ==========================================

print("\nDatabase File")
print("-" * 35)
print(DB_PATH)

print("\nSQLite Database Loaded Successfully!")