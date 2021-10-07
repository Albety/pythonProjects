import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("country_data.csv")
print(data.head())

life_expectancy = data['Life Expectancy']
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])
life_expectancy_iqr = stats.iqr(life_expectancy)

plt.hist(life_expectancy)
plt.show()

gdp = data['GDP']
median_gdp = np.quantile(gdp, 0.5)
low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] > median_gdp]

low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'], [0.25,0.5,0.75])
high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'], [0.25,0.5,0.75])
