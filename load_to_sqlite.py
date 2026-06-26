from sqlalchemy import create_engine, text
import pandas as pd

# Create SQLite database connection
engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

# ==========================
# Read CSV Files
# ==========================

fund = pd.read_csv(
    "data/raw/Bluestock_MF_Datasets/01_fund_master.csv"
)

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

transactions = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

performance = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

aum = pd.read_csv(
    "data/raw/Bluestock_MF_Datasets/03_aum_by_fund_house.csv"
)

# ==========================
# Load into SQLite
# ==========================

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

# ==========================
# Verify CSV Row Counts
# ==========================

print("\nCSV Row Counts")
print("--------------------------")
print("dim_fund:", len(fund))
print("fact_nav:", len(nav))
print("fact_transactions:", len(transactions))
print("fact_performance:", len(performance))
print("fact_aum:", len(aum))

# ==========================
# Verify Database Row Counts
# ==========================

print("\nDatabase Row Counts")
print("--------------------------")

with engine.connect() as conn:

    print(
        "dim_fund:",
        conn.execute(
            text("SELECT COUNT(*) FROM dim_fund")
        ).scalar()
    )

    print(
        "fact_nav:",
        conn.execute(
            text("SELECT COUNT(*) FROM fact_nav")
        ).scalar()
    )

    print(
        "fact_transactions:",
        conn.execute(
            text("SELECT COUNT(*) FROM fact_transactions")
        ).scalar()
    )

    print(
        "fact_performance:",
        conn.execute(
            text("SELECT COUNT(*) FROM fact_performance")
        ).scalar()
    )

    print(
        "fact_aum:",
        conn.execute(
            text("SELECT COUNT(*) FROM fact_aum")
        ).scalar()
    )

print("\nSQLite Database Loaded Successfully!")