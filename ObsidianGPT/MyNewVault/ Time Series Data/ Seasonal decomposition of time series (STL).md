#  Seasonal decomposition of time series (STL)
**Model Type:**  Forecasting Models
**Data Type:**  Time Series Data

**Python code **:


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL

# Load an example time series dataset (monthly passenger airline data)
data = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv")
data['Month'] = pd.to_datetime(data['Month'])
data.set_index('Month', inplace=True)

# Perform STL decomposition
stl = STL(data['Passengers'], seasonal=13)
result = stl.fit()

# Plot the original time series and the decomposed components
fig, ax = plt.subplots(4, 1, figsize=(12, 6), sharex=True)
ax[0].plot(data['Passengers'], label='Original Time Series')
ax[0].legend()
ax[1].plot(result.trend, label='Trend Component')
ax[1].legend()
ax[2].plot(result.seasonal, label='Seasonal Component')
ax[2].legend()
ax[3].plot(result.resid, label='Residual Component')
ax[3].legend()
plt.show()
```
This code demonstrates how to perform STL decomposition on a dataset of monthly passenger airline data. It uses the statsmodels library and plots the original time series along with its decomposed trend, seasonal, and residual components.


**See Also**:

- [[ Autoregressive Integrated Moving Average (ARIMA)]]
- [[ Recurrent Neural Networks (RNN)]]
- [[ Long Short]]
- [[ Gated Recurrent Units (GRU)]]
- [[ Facebook Prophet]]
- [[ LightGBM]]
- [[ XGBoost]]
## Resources

a. Python's statsmodels library provides a simple implementation of STL decomposition. The official documentation provides an example and explanation: https://www.statsmodels.org/stable/examples/notebooks/generated/stl_decomposition.html
b. The book "Forecasting: principles and practice" by Rob J. Hyndman and George Athanasopoulos provides a comprehensive introduction to STL and other techniques for time series decomposition and forecasting: https://otexts.com/fpp2/stl.html
c. This tutorial gives a step-by-step explanation of how to perform and interpret STL decomposition in Python: https://towardsdatascience.com/decompose-time-series-data-trend-seasonality-moving-average-and-a-robust-approach-bdef7c212c68


---
tags: #-time-series-data, #-time-series-data/-seasonal-decomposition-of-time-series-stl
