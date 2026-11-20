# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:14:20 2026

@author: adria
"""

import pandas as pd
import numpy as np
from pathlib import Path  

dates = pd.date_range(start="2023-01-01", periods=250, freq="B")

data = {
    "Date": dates,
    "Index_STOXX600": np.cumprod(1 + np.random.normal(0.0001, 0.01, 250)) * 400,
    "Stock_APPLE": np.cumprod(1 + np.random.normal(0.0002, 0.02, 250)) * 150,
    "Stock_NESTLE": np.cumprod(1 + np.random.normal(0.0001, 0.015, 250)) * 100,
    "Stock_NOVARTIS": np.cumprod(1 + np.random.normal(0.0001, 0.012, 250)) * 80
}

data_df = pd.DataFrame(data)
generated_data_path = Path('data') / 'stoxx600_prices_generated_data.csv'
data_df.to_csv(generated_data_path, index=False)

"""
df is dataframe

"""
print(f"Success, saved in: {generated_data_path}")