#  Autoregressive Integrated Moving Average (ARIMA)
**Model Type:**  Forecasting Models
**Data Type:**  Time Series Data

**Python code **:


```python
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load and Basic Analysis
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"
df = pd.read_csv(url, parse_dates=[0], index_col=0)
print(df.head())

# Visualize the Time Series Data
plt.plot(df)
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Daily Minimum Temperatures (1981-1990)")
plt.show()

# Design and Fit ARIMA Model
arima_model = ARIMA(df, order=(5,1,1)).fit()

# Model Summary
print(arima_model.summary())

# Make Forecast
n_periods = 30
forecast, std_error, conf_interval = arima_model.forecast(steps=n_periods, alpha=0.05)

# Visualize Forecast
idx = pd.date_range(df.index[-1]+pd.Timedelta(days=1), periods=n_periods, freq="D")
forecast_series = pd.Series(forecast, index=idx)

plt.plot(df[-100:], label="Observed", marker=".")
plt.plot(forecast_series, label="Forecast", marker=".")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.legend()
plt.title("Daily Minimum Temperature Forecast (Next 30 Days)")
plt.show()
```
This code demonstrates the use of the ARIMA model for time series forecasting. It loads a dataset containing daily minimum temperatures, visualizes the data, and creates an ARIMA(5,1,1) model. The model is then used to make forecasts for the next 30 days, and the forecasts are visualized alongside the observed temperature for comparison.


**See Also**:

- [[ Seasonal decomposition of time series (STL)]]
- [[ Recurrent Neural Networks (RNN)]]
- [[ Long Short]]
- [[ Gated Recurrent Units (GRU)]]
- [[ Facebook Prophet]]
- [[ LightGBM]]
- [[ XGBoost]]
## Resources

a. The ARIMA model in-depth explanation and Python examples: https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
b. Time Series Forecasting with ARIMA in Python: https://www.datacamp.com/community/tutorials/time-series-analysis-tutorial
c. Statsmodels ARIMA documentation: https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html


---
tags: #-time-series-data, #-time-series-data/-autoregressive-integrated-moving-average-arima
