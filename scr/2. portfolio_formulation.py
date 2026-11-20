# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:47:43 2026

@author: adria
"""
import pandas as pd
from pathlib import Path

# 1. Set the data folder path and load the calculated betas
calculated_betas_path = Path('intermediary_steps') / 'calculated_betas.csv'
df_betas = pd.read_csv(calculated_betas_path)

# 2. Find the median (the exact midpoint of the betas)
median_beta = df_betas['Beta'].median()
print(f"The median Beta is: {median_beta:.4f}\n")

# 3. Split the companies into two teams (Long and Short)
# Long Portfolio (Low Betas - Safe stocks to BUY)
portfolio_long = df_betas[df_betas['Beta'] <= median_beta].copy()

# Short Portfolio (High Betas - Volatile stocks to SELL)
portfolio_short = df_betas[df_betas['Beta'] > median_beta].copy()

print(f"LONG PORTFOLIO (Buy safe stocks): {len(portfolio_long)} companies")
print(portfolio_long)
print("\n--------------------------------------------------\n")
print(f"SHORT PORTFOLIO (Sell volatile stocks): {len(portfolio_short)} companies")
print(portfolio_short)

# 4. Save the two portfolios into files for the next step
folder_path = Path('intermediary_steps')
long_portfolio_path = folder_path / 'long_portfolio.csv'
short_portfolio_path = folder_path / 'short_portfolio.csv'
portfolio_long.to_csv(long_portfolio_path , index=False)
portfolio_short.to_csv(short_portfolio_path, index=False)
"""
index=False due to not wanting the index to appear in the data frame as a colum
"""
#NOT REALLY PORTFOLIOS (THERE ARE NOT WEIGHTS YET TO DETERMINE A STRATEGY OF INVESTMENT), JUST DATA (STOCKS WITH THEIR RESPECTIVE BETA)
print(f"\nPortfolios successfully saved in {folder_path} ")