# Data Dictionary – Mutual Fund Analytics Capstone

## Overview

This document describes the datasets, columns, data types, business meanings, and source references used in the Mutual Fund Analytics project.

---

# 1. Fund Master Dataset

**Source File:** `01_fund_master.csv`

| Column Name        | Data Type | Business Definition                |
| ------------------ | --------- | ---------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier      |
| fund_house         | Text      | Mutual fund company name           |
| scheme_name        | Text      | Name of the mutual fund scheme     |
| category           | Text      | Fund category (Equity, Debt, etc.) |
| sub_category       | Text      | Fund sub-category                  |
| plan               | Text      | Direct or Regular plan             |
| launch_date        | Date      | Scheme launch date                 |
| benchmark          | Text      | Benchmark index used               |
| expense_ratio_pct  | Float     | Fund management fee percentage     |
| exit_load_pct      | Float     | Exit load charged on redemption    |
| min_sip_amount     | Integer   | Minimum SIP investment amount      |
| min_lumpsum_amount | Integer   | Minimum lump-sum investment        |
| fund_manager       | Text      | Fund manager name                  |
| risk_category      | Text      | Risk classification                |
| sebi_category_code | Text      | SEBI category code                 |

---

# 2. NAV History Dataset

**Source File:** `02_nav_history.csv`

| Column Name | Data Type | Business Definition     |
| ----------- | --------- | ----------------------- |
| amfi_code   | Integer   | Mutual fund AMFI code   |
| nav_date    | Date      | NAV calculation date    |
| nav         | Float     | Net Asset Value of fund |

---

# 3. AUM Dataset

**Source File:** `03_aum_by_fund_house.csv`

| Column Name | Data Type | Business Definition               |
| ----------- | --------- | --------------------------------- |
| fund_house  | Text      | Mutual fund company               |
| aum_crore   | Float     | Assets Under Management (₹ Crore) |

---

# 4. Monthly SIP Inflows Dataset

**Source File:** `04_monthly_sip_inflows.csv`

| Column Name      | Data Type | Business Definition       |
| ---------------- | --------- | ------------------------- |
| month            | Date      | Reporting month           |
| sip_amount_crore | Float     | Monthly SIP inflow amount |

---

# 5. Category Inflows Dataset

**Source File:** `05_category_inflows.csv`

| Column Name  | Data Type | Business Definition |
| ------------ | --------- | ------------------- |
| category     | Text      | Fund category       |
| inflow_crore | Float     | Net inflow amount   |

---

# 6. Industry Folio Count Dataset

**Source File:** `06_industry_folio_count.csv`

| Column Name | Data Type | Business Definition   |
| ----------- | --------- | --------------------- |
| month       | Date      | Reporting month       |
| folio_count | Integer   | Total investor folios |

---

# 7. Scheme Performance Dataset

**Source File:** `07_scheme_performance.csv`

| Column Name        | Data Type | Business Definition           |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Mutual fund AMFI code         |
| scheme_name        | Text      | Fund scheme name              |
| fund_house         | Text      | Mutual fund company           |
| category           | Text      | Fund category                 |
| plan               | Text      | Direct/Regular                |
| return_1yr_pct     | Float     | 1-Year return (%)             |
| return_3yr_pct     | Float     | 3-Year return (%)             |
| return_5yr_pct     | Float     | 5-Year return (%)             |
| benchmark_3yr_pct  | Float     | Benchmark return (%)          |
| alpha              | Float     | Excess return over benchmark  |
| beta               | Float     | Market risk measure           |
| sharpe_ratio       | Float     | Risk-adjusted return metric   |
| sortino_ratio      | Float     | Downside risk-adjusted return |
| std_dev_ann_pct    | Float     | Annualized volatility         |
| max_drawdown_pct   | Float     | Maximum decline from peak     |
| aum_crore          | Float     | Assets Under Management       |
| expense_ratio_pct  | Float     | Fund expense ratio            |
| morningstar_rating | Integer   | Morningstar rating            |
| risk_grade         | Text      | Fund risk grade               |

---

# 8. Investor Transactions Dataset

**Source File:** `08_investor_transactions.csv`

| Column Name        | Data Type | Business Definition        |
| ------------------ | --------- | -------------------------- |
| investor_id        | Text      | Unique investor identifier |
| transaction_date   | Date      | Transaction date           |
| amfi_code          | Integer   | Mutual fund scheme code    |
| transaction_type   | Text      | SIP, Lumpsum, Redemption   |
| amount_inr         | Float     | Transaction amount         |
| state              | Text      | Investor state             |
| city               | Text      | Investor city              |
| city_tier          | Text      | Tier classification        |
| age_group          | Text      | Investor age group         |
| gender             | Text      | Investor gender            |
| annual_income_lakh | Float     | Annual income in lakhs     |
| payment_mode       | Text      | Payment method             |
| kyc_status         | Text      | KYC verification status    |

---

# 9. Portfolio Holdings Dataset

**Source File:** `09_portfolio_holdings.csv`

| Column Name | Data Type | Business Definition             |
| ----------- | --------- | ------------------------------- |
| amfi_code   | Integer   | Fund scheme code                |
| stock_name  | Text      | Holding company name            |
| sector      | Text      | Industry sector                 |
| weight_pct  | Float     | Portfolio allocation percentage |

---

# 10. Benchmark Indices Dataset

**Source File:** `10_benchmark_indices.csv`

| Column Name | Data Type | Business Definition  |
| ----------- | --------- | -------------------- |
| index_name  | Text      | Benchmark index name |
| index_date  | Date      | Index date           |
| index_value | Float     | Benchmark value      |

---

# Data Quality Notes

* Missing values checked and validated.
* Duplicate records removed from cleaned datasets.
* NAV values validated to be positive.
* Transaction amounts validated to be greater than zero.
* Expense ratios validated within acceptable range.
* Return metrics converted to numeric data types.
* Date columns standardized using Pandas datetime functions.

---

# Database Tables

| Table Name        | Purpose                       |
| ----------------- | ----------------------------- |
| dim_fund          | Fund master dimension         |
| dim_date          | Date dimension                |
| fact_nav          | Daily NAV facts               |
| fact_transactions | Investor transaction facts    |
| fact_performance  | Fund performance facts        |
| fact_aum          | Assets Under Management facts |
