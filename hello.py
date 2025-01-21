import pandas as pd
import numpy as np

Auto = pd.read_csv('Auto.csv', na_values=['?', '0'])
Auto.fillna(0, inplace=True)

print(Auto['horsepower'].sum())
print(Auto.shape)
print(Auto.columns)

idx_80 = Auto['year'] > 80
print(Auto[idx_80])

print(Auto[['horsepower', 'year']])