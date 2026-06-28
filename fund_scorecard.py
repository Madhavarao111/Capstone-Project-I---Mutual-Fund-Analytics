import pandas as pd

# Load datasets
cagr = pd.read_csv("data/processed/cagr_table.csv")

sharpe = pd.read_csv("data/processed/sharpe_ratio.csv")

alpha = pd.read_csv("data/processed/alpha_beta.csv")

drawdown = pd.read_csv("data/processed/maximum_drawdown.csv")

performance = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Keep only required columns
cagr = cagr[["amfi_code", "CAGR_3Y"]]
sharpe = sharpe[["amfi_code", "Sharpe_Ratio"]]
alpha = alpha[["amfi_code", "Alpha"]]
drawdown = drawdown[["amfi_code", "Maximum_Drawdown (%)"]]
performance = performance[["amfi_code", "scheme_name", "expense_ratio_pct"]]


# Merge all datasets
scorecard = performance.merge(
    cagr,
    on="amfi_code"
).merge(
    sharpe,
    on="amfi_code"
).merge(
    alpha,
    on="amfi_code"
).merge(
    drawdown,
    on="amfi_code"
)

# Create ranks

# Higher CAGR is better
scorecard["cagr_rank"] = (scorecard["CAGR_3Y"].rank(ascending=False))

# Higher Sharpe is better
scorecard["sharpe_rank"] = (scorecard["Sharpe_Ratio"].rank(ascending=False))

# Higher Alpha is better
scorecard["alpha_rank"] = (scorecard["Alpha"].rank(ascending=False))

# Lower expense ratio is better
scorecard["expense_rank"] = (scorecard["expense_ratio_pct"].rank(ascending=True))

# Smaller drawdown is better
scorecard["drawdown_rank"] = (scorecard["Maximum_Drawdown (%)"].rank(ascending=False))

# Convert ranks into weighted scores
scorecard["Fund_Score"] = (
      scorecard["cagr_rank"] * 0.30
    + scorecard["sharpe_rank"] * 0.25
    + scorecard["alpha_rank"] * 0.20
    + scorecard["expense_rank"] * 0.15
    + scorecard["drawdown_rank"] * 0.10
)

# Since lower weighted rank is better,
# sort ascending
scorecard = scorecard.sort_values("Fund_Score")

# Final Rank
scorecard["Overall_Rank"] = range(1,len(scorecard) + 1)

# Convert score to 0–100
max_score = scorecard["Fund_Score"].max()
min_score = scorecard["Fund_Score"].min()

scorecard["Score_100"] = ((max_score - scorecard["Fund_Score"])
    /(max_score - min_score)) * 100

scorecard["Score_100"] = scorecard["Score_100"].round(2)

# Display output
print("\nFund Scorecard")
print(scorecard[["Overall_Rank","amfi_code","scheme_name","Score_100"]])

# Save CSV
scorecard.to_csv("data/processed/fund_scorecard.csv",index=False)

print("\nFund Scorecard created successfully!")