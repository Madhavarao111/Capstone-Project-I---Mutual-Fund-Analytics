import pandas as pd

# Load cleaned NAV history
df = pd.read_csv("data/processed/nav_daily_returns.csv")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# sort by scheme and date
df = df.sort_values(['amfi_code', 'date'])

results = []

# Calculate CAGR for each scheme

# Process each mutual fund separately
for code, group in df.groupby('amfi_code'):
    #sort records by date
    group = group.sort_values('date')

    # latest NAV and latest date
    latest_date = group['date'].max()
    latest_nav = group.iloc[-1]['nav']

    # Store result for one fund
    fund_result = {"amfi_code": code}

    #caluculate CAGR for 1 year, 3 years, and 5 years
    for years in [1, 3, 5]:
        #target date for the given year
        target_date = latest_date - pd.DateOffset(years=years)

        #find nav closest to the target date
        historical_data = group[group['date'] <= target_date]

        if historical_data.empty:
            #no data available for the target date, set CAGR to None
            fund_result[f'cagr_{years}yr'] = None
        else:
            #start nav
            start_nav = historical_data.iloc[-1]['nav']

            #cagr calculation
            cagr = ((latest_nav / start_nav) ** (1 / years)) - 1

            #convert to percentage and round to 2 decimal places
            fund_result[f"CAGR_{years}Y"] = round(cagr * 100, 2)
            
    results.append(fund_result)

#create comparison table
cagr_df = pd.DataFrame(results)

#sort by amfi_code
cagr_df = cagr_df.sort_values('amfi_code')

#display results
print("\nCAGR Comparison Table")
print(cagr_df)

# Save CAGR results to CSV
cagr_df.to_csv("data/processed/cagr_table.csv", index=False)

print("\nCAGR calculation completed successfully!")
