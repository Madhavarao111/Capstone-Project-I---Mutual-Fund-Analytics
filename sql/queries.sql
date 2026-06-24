-- 1. Top 5 Funds by AUM

SELECT
fund_house,
aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV Per Month

SELECT
strftime('%Y-%m', nav_date) AS month,
ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. SIP Year-over-Year Growth

SELECT
strftime('%Y', transaction_date) AS year,
SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY year
ORDER BY year;

-- 4. Transactions by State

SELECT
state,
COUNT(*) AS total_transactions,
ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with Expense Ratio Less Than 1%

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Top 10 Funds by 1-Year Return

SELECT
scheme_name,
return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- 7. Average Investment Amount by Transaction Type

SELECT
transaction_type,
ROUND(AVG(amount_inr), 2) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 8. Fund Count by Category

SELECT
category,
COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;


-- 9. Risk Category Distribution

SELECT
risk_category,
COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_category
ORDER BY total_funds DESC;

-- 10. Top 5 Funds by Sharpe Ratio

SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;
