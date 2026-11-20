# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:57:35 2026

@author: adria
"""

import pandas as pd
from pathlib import Path

# 1. Set the folder path and load the Long and Short portfolios from Step 3
folder_path = Path('intermediary_steps')

long_path = folder_path / 'long_portfolio.csv'
short_path = folder_path / 'short_portfolio.csv'

portfolio_long = pd.read_csv(long_path)
portfolio_short = pd.read_csv(short_path)

# 2. Calculate the average Beta of each team
mean_beta_long = portfolio_long['Beta'].mean()
mean_beta_short = portfolio_short['Beta'].mean()

print(f"Average Beta of Long Team (Safe): {mean_beta_long:.4f}")
print(f"Average Beta of Short Team (Risky): {mean_beta_short:.4f}\n")

# 3. Calculate the investment multiplier (Weight) to make total Beta = 1
# Formula: 1 / Average Beta
weight_long_total = 1.0 / mean_beta_long
weight_short_total = 1.0 / mean_beta_short

print(f"Total Money Multiplier for Long Team: {weight_long_total:.2f}x (Leverage applied)")
print(f"Total Money Multiplier for Short Team: {weight_short_total:.2f}x (De-leveraged)\n")

# 4. Assign the weight equally to each individual stock inside the team

# We divide the total multiplier by the number of companies in the team
# Long weights are positive (buying), Short weights are negative (selling)
num_long_stocks = len(portfolio_long)
num_short_stocks = len(portfolio_short)
portfolio_long['Weight'] = weight_long_total / num_long_stocks
portfolio_short['Weight'] = -(weight_short_total / num_short_stocks)

#NOW THEY ARE (SPECIFIC) PORTFOLIOS
"""
portfolio_long['Weight'] = weight_long_total / num_long_stocks
portfolio_short['Weight'] = -(weight_short_total / num_short_stocks)
are adding the Weight column to each one
"""

# 5. Combine both teams into a single final master portfolio
final_portfolio = pd.concat([portfolio_long, portfolio_short], ignore_index=True)

print("--- FINAL PORTFOLIO ---")
print(final_portfolio)

# 6. Save the final weighted portfolio
final_weights_path = folder_path / 'final_portfolio_weights.csv'
final_portfolio.to_csv(final_weights_path, index=False)
print(f"\nFinal portfolio weights successfully saved in '{final_weights_path}'!")