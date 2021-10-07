import pandas as pd
import numpy as np
from scipy import stats
from weather_data import london_data

print(london_data.head())

temp = london_data['TemperatureC']
average_temp = np.average(temp)
median_temp = np.median(temp)
mode_temp = stats.mode(temp)

temperature_var = np.var(temp)
temperature_standard_deviation = np.std(temp)

june = london_data[london_data["month"] == 6]["TemperatureC"]
july = london_data[london_data["month"] == 7]["TemperatureC"]

for i in range(1, 13):
  month = london_data[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")