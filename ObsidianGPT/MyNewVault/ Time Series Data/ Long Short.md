#  Long Short
**Model Type:**  Exponential Smoothing State Space Models (ETS)
**Data Type:**  Time Series Data

**Python code **:


```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download stock data
data = yf.download("AAPL GOOGL MSFT", start="2020-01-01", end="2021-01-01")['Close']

# Calculate the returns
returns = data.pct_change()

# Calculate the mean returns and standard deviations
mean_returns = returns.mean()
std_returns = returns.std()

# Create a simple scoring system (higher score means larger long position, lower score means larger short)
scores = (mean_returns - std_returns).rank()

# Normalize the scores to determine the weight of each stock
weights = scores / scores.sum()

# Create a portfolio with these weights
portfolio = (weights * returns).sum(axis=1)

# Calculate the cumulative returns of the portfolio
cumulative_returns = (1 + portfolio).cumprod()

# Plot the cumulative returns
import matplotlib.pyplot as plt
cumulative_returns.plot()
plt.show()
```

This code demonstrates a simple Long-Short model using Python with yfinance for stock data, where the stocks are ranked based on their mean return minus their standard deviation, and the normalized ranking scores are used as the weights for the positions. This model can be further extended to include other factors and strategies, depending on the user's goals and preferences.


**See Also**:

- [[ Autoregressive Integrated Moving Average (ARIMA)]]
- [[ Seasonal decomposition of time series (STL)]]
- [[ Recurrent Neural Networks (RNN)]]
- [[ Gated Recurrent Units (GRU)]]
- [[ Facebook Prophet]]
- [[ LightGBM]]
- [[ XGBoost]]
## Resources

- Investopedia: Offers an introduction to the Long-Short model and the concept of market neutrality (https://www.investopedia.com/terms/l/long-shortequity.asp)
- QuantInsti: Learn how to implement a Long-Short strategy using Python (https://blog.quantinsti.com/long-short-equity/)
- Seeking Alpha: An overview of various Long-Short strategies and their applications (https://seekingalpha.com/article/4403698-long-or-short-equity-strategies)


---
tags: #-time-series-data, #-time-series-data/-long-short
