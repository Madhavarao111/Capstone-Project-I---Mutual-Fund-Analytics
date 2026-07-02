from pathlib import Path
import pandas as pd

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load datasets
fund_master = pd.read_csv(
    BASE_DIR / "data" / "raw" / "Bluestock_MF_Datasets" / "01_fund_master.csv"
)

sharpe = pd.read_csv(
    BASE_DIR / "data" / "processed" / "sharpe_ratio.csv"
)

# Merge datasets
recommendation = fund_master.merge(
    sharpe,
    on="scheme_name",
    how="inner"
)

# User input
risk = input("Enter Risk Appetite (Low/Moderate/High): ").strip().lower()

# Filter funds
if risk == "low":
    filtered = recommendation[
        recommendation["risk_category"] == "Low"
    ]

elif risk == "moderate":
    filtered = recommendation[
        recommendation["risk_category"].isin(
            ["Moderate", "Moderately High"]
        )
    ]

elif risk == "high":
    filtered = recommendation[
        recommendation["risk_category"].isin(
            ["High", "Very High"]
        )
    ]

else:
    print("Invalid Risk Level!")
    exit()

# Top 3 funds
top3 = filtered.sort_values(
    by="sharpe_ratio",
    ascending=False
).head(3)

print("\n" + "=" * 70)
print("Top 3 Recommended Mutual Funds")
print("=" * 70)

print(
    top3[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_category",
            "sharpe_ratio"
        ]
    ]
)

# Save output
output_file = BASE_DIR / "data" / "processed" / "fund_recommendation.csv"

top3.to_csv(output_file, index=False)

print(f"\n✅ Recommendation saved to:\n{output_file}")