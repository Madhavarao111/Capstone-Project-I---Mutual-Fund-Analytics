-- Top 5 funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum_cr DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Expense ratio below 1%
SELECT *
FROM dim_fund
WHERE expense_ratio_pct < 1;