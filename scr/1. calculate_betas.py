# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:23:00 2026

@author: adria
"""

import pandas as pd
import numpy as np
from pathlib import Path

# 1. Load the generated data
csv_path = Path('data')/ 'stoxx600_prices_generated_data.csv'
df = pd.read_csv(csv_path, index_col='Date', parse_dates=True)

"""
index_col='Date': Tells Python that the column named "Date" is not regular data, but the main index (the spine or row labels of the table). This ensures every single row is identified by its specific day.

parse_dates=True: Tells Python: "Pay attention, the items in the index are real calendar dates, not just plain text." This is crucial so the program understands the chronological flow of time (which day comes before or after another).


"""

# 2. Calculate daily percentage returns
returns = df.pct_change().dropna()

"""
.pct_change(): A built-in Pandas formula. It takes today's price, compares it to yesterday's price, and automatically calculates the percentage it went up or down. It does this all at once for the entire year and for every stock in the table.

.dropna(): Stands for "Drop Not Available" (delete missing values). Think about the very first day in your dataset (e.g., January 1st). Because there is no previous day in the table to compare it to, Python cannot calculate a percentage change for that specific day, resulting in a missing value (NaN). This command simply deletes that first blank row so it does not break the mathematical calculations later in the project.

"""

# 3. Separate the index (market) from the stocks
market_returns = returns['Index_STOXX600']
stock_returns = returns.drop(columns=['Index_STOXX600'])

# 4. Calculate the Beta for each stock
betas = {}
var_market = market_returns.var()

for col in stock_returns.columns:
    cov_stock_market = stock_returns[col].cov(market_returns)
    beta = cov_stock_market / var_market
    betas[col] = beta
"""
The variable col temporarily holds the name of the current company being analyzed (for example, "Stock_APPLE").

This calculates the "covariance" (.cov()) between the specific stock and the overall market index. Covariance is a statistical tool that measures how closely the daily price changes of this stock match the daily price changes of the market.
(HAVE IN MIND, ARE TWO COLUMS)

What it does: It takes that final Beta number and saves it inside the betas dictionary
"""

# 5. Display results
df_betas = pd.DataFrame(list(betas.items()), columns=['Stock', 'Beta'])
print("\n--- CALCULATED BETAS ---")
print(df_betas)
"""
betas.items(): The betas variable is a Python dictionary (which stores data in pairs, like Company: Beta). This command extracts all those pairs together (e.g., "Apple" and "1.12").

list(...): This takes those extracted pairs and bundles them into a standard, ordered Python list so that Pandas can read them easily.

pd.DataFrame(...): This is the core Pandas command that takes your raw list of data and transforms it into a clean, two-dimensional table (a DataFrame) with rows and columns.

columns=['Stock', 'Beta']: This assigns specific names to the columns of your new table. The company names will go under the header "Stock", and their corresponding risk numbers will go under "Beta".

df_betas = : Finally, this saves the fully built table into a new variable named

"""

# Save the calculated betas for the next step
calculated_betas_path = Path('intermediary_steps') / 'calculated_betas.csv'
df_betas.to_csv(calculated_betas_path, index=False)
print(f"\nBetas successfully saved in {calculated_betas_path}")