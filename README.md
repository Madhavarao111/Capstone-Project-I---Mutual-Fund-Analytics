# Mutual Fund Analytics — Capstone Project I

*An End-to-End Data Analytics Platform for Fund Performance, Risk & Investor Behaviour Analysis*

## Overview

This project builds a complete analytics pipeline over a simulated but realistic Indian mutual fund dataset — **40 schemes across 10 fund houses** — covering NAV history, AUM, SIP inflows, investor transactions, portfolio holdings, and benchmark indices.

Raw CSVs are ingested and validated, cleaned with Pandas, and loaded into a SQLite **star-schema** database. Jupyter notebooks then compute standard and advanced performance/risk metrics, and the results are consolidated into an interactive **Power BI dashboard**.

**Dataset scale:** 46,000+ NAV records · 32,778 investor transactions · 12 sub-categories · Equity (34) & Debt (6) schemes.

## Key Features

- **ETL Pipeline** — orchestrated ingestion → cleaning → SQLite load, with lossless row-count verification at each stage
- **Star-Schema Database** — `dim_fund` plus four fact tables (`fact_nav`, `fact_transactions`, `fact_performance`, `fact_aum`)
- **Performance Analytics** — Daily Returns, CAGR, Sharpe Ratio, Sortino Ratio, Alpha, Beta, Maximum Drawdown, and a composite Fund Scorecard
- **Advanced Analytics** — Historical VaR & CVaR, 90-day Rolling Sharpe Ratio, Sector HHI concentration, Investor Cohort Analysis, SIP Continuity / At-Risk flagging, Tracking Error, and a simple risk-based Fund Recommender
- **Power BI Dashboard** — 5 report pages: Industry Overview, Fund Performance, Investor Analytics, SIP & Market Trends, NAV Detail

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Data Processing | Pandas, NumPy |
| Statistics | SciPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Database | SQLite + SQLAlchemy |
| Notebooks | Jupyter |
| Dashboard / BI | Microsoft Power BI |
| Live Data | Requests + mfapi.in API |

## Project Structure

```
Capstone Project I - Mutual Fund Analytics/
├── data/
│   ├── raw/
│   │   ├── Bluestock_MF_Datasets/     # 10 source CSVs
│   │   └── live_nav/                  # Live NAV pulled from mfapi.in (6 schemes)
│   ├── processed/                     # Cleaned CSVs + computed metric outputs
│   └── db/
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb.ipynb
│   └── 05_advanced_analytics.ipynb.ipynb
├── scripts/
│   ├── etl_pipeline.py                # Orchestrates the full ETL run
│   ├── compute_metrics.py             # Orchestrates performance metric scripts
│   ├── live_nav_fetch.py
│   └── recommender.py
├── sql/
│   ├── schema.sql                     # Star-schema DDL
│   └── queries.sql                    # 10 analytical queries
├── dashboard/
│   └── Bluestock_Mutual_Fund_Dashboard/
│       ├── bluestock_mf_dashboard.pbix
│       ├── Dashboard.pdf
│       └── 01–05_*.png                # Exported report page images
├── reports/
│   ├── data_dictionary.md
│   ├── day1_data_quality.md
│   ├── rolling_sharpe_chart.png
│   ├── sector_hhi_chart.png
│   └── Presentation.pptx
├── clean_nav_history.py / clean_transactions.py / clean_scheme_performance.py
├── create_database.py / load_to_sqlite.py
├── daily_returns.py / cagr_calculation.py / sharpe_ratio.py / sortino_ratio.py
├── alpha_beta.py / maximum_drawdown.py / fund_scorecard.py / benchmark_comparison.py
├── amfi_validation.py / check_transactions.py
├── bluestock_mf.db                    # SQLite database
├── requirements.txt
└── README.md
```

## Database Schema (Star Schema)

| Table | Type | Key Columns | Rows |
|---|---|---|---|
| `dim_fund` | Dimension | amfi_code (PK), fund_house, scheme_name, category, sub_category, risk_category | 40 |
| `fact_nav` | Fact | nav_id (PK), amfi_code (FK), nav_date, nav | 46,000 |
| `fact_transactions` | Fact | txn_id (PK), investor_id, amfi_code (FK), transaction_type, amount_inr, transaction_date | 32,778 |
| `fact_performance` | Fact | perf_id (PK), amfi_code (FK), return_1y, return_3y, return_5y | 40 |
| `fact_aum` | Fact | aum_id (PK), fund_house, aum_cr | 90 |

Defined in `sql/schema.sql`; a library of 10 analytical queries lives in `sql/queries.sql`.

## Getting Started

### Prerequisites

- Python 3.11+
- Power BI Desktop (to open `dashboard/Bluestock_Mutual_Fund_Dashboard/bluestock_mf_dashboard.pbix`)

### Installation

```bash
pip install -r requirements.txt
```

### Running the Pipeline

```bash
# 1. Run the ETL pipeline (clean + load to SQLite)
python scripts/etl_pipeline.py

# 2. Compute standard performance metrics
python scripts/compute_metrics.py

# 3. Explore analyses interactively
jupyter notebook notebooks/
```

The ETL pipeline runs `clean_nav_history.py → clean_transactions.py → clean_scheme_performance.py → load_to_sqlite.py`, cross-validating CSV row counts against the resulting database tables to confirm a lossless load.

## Key Results & Insights

- AUM is concentrated among a handful of large fund houses — SBI, ICICI Prudential, HDFC, and Nippon India account for the majority of average AUM.
- The scheme universe skews Equity-heavy (34/40) and Moderate-to-High risk (28/40).
- The composite **Fund Scorecard** places Mirae Asset Large Cap Fund at the top (Score 100.00, 34.00% CAGR, Sharpe 1.4483) — demonstrating that risk-adjusted ranking can reorder funds versus raw returns alone.
- Small Cap schemes carry the highest tail risk by VaR/CVaR.
- SIP is the dominant transaction type by count (~60%), though Lumpsum and Redemption transactions carry ~23x larger average ticket sizes.
- 98% of frequent SIP investors (1,332 of 1,362) show irregular contribution gaps, flagging them "At Risk" of discontinuation.
- Portfolio concentration (HHI) varies meaningfully even within similarly categorized equity funds.

See `reports/data_dictionary.md`, `reports/day1_data_quality.md`, and the full **Final_Report.docx** / `reports/Presentation.pptx` for complete details.

## Future Scope

- Extend live NAV integration to all 40 schemes on a scheduled basis
- Replace the rule-based recommender with an ML model incorporating investor risk profile and behaviour
- Train a predictive SIP-discontinuation classification model
- Migrate from SQLite to PostgreSQL or a cloud data warehouse
- Automate pipeline orchestration with Apache Airflow or Prefect
- Extend HHI to full portfolio overlap analysis with factor-based attribution
- Build a lightweight web-based self-service dashboard (Streamlit / Flask)

## References

- [AMFI](https://www.amfiindia.com) — Official mutual fund industry data and NAV disclosure standards
- [mfapi.in](https://www.mfapi.in) — Public REST API used for live NAV retrieval
- Bluestock Mutual Fund Datasets — capstone dataset source
- [Pandas](https://pandas.pydata.org/docs/) · [SQLAlchemy](https://docs.sqlalchemy.org/) · [Power BI](https://learn.microsoft.com/power-bi/) documentation
