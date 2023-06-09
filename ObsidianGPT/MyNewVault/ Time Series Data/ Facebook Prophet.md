**Model Type:**  Exponential Smoothing State Space Models (ETS)
**Data Type:**  Time Series Data

## Use Cases :

a. Sales forecasting: When businesses have historical sales data that exhibits seasonal patterns and trends, Prophet can be effectively used to predict future sales.

b. Inventory management: Prophet can help predict future inventory requirements by analyzing historical product demand patterns, which can assist in managing stock levels and reducing inventory costs.

c. Resource planning: Businesses can identify trends and periodic patterns in their workload to allocate resources and enhance productivity using Prophet for forecasting future workloads.


## Python code: 

```python
import pandas as pd
from fbprophet import Prophet

# Load the example data
df = pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/master/examples/example_wp_log_peyton_manning.csv')

# Rename the columns to 'ds' and 'y' (required by Prophet)
df = df.rename(columns={'Date': 'ds', 'Sales': 'y'})

# Instantiate the Prophet model
model = Prophet()

# Fit the model on the historical data
model.fit(df)

# Make future predictions for the next 365 days
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

# Plot the forecast
fig1 = model.plot(forecast)
```

Make sure to install the necessary library first with `!pip install fbprophet`.


## Resources

a. The official Facebook Prophet documentation serves as an excellent guide on how to build models using it and make forecasts. (https://facebook.github.io/prophet/docs/quick_start.html)
b. This Medium post by Benjamin Ayanian walks through building a time series forecast model using Python and Facebook Prophet with a practical example. (https://medium.com/analytics-vidhya/time-series-forecasting-with-facebook-prophet-in-python-bd190191146e)
c. This YouTube video by the Data Professor provides a hands-on tutorial for building a time series forecasting model using Facebook Prophet. (https://www.youtube.com/watch?v=d4noqr0I5H0)

**See Also**:

- [[ Autoregressive Integrated Moving Average (ARIMA)]]
- [[ Seasonal decomposition of time series (STL)]]
- [[ Recurrent Neural Networks (RNN)]]
- [[ Long Short]]
- [[ Gated Recurrent Units (GRU)]]
- [[ LightGBM]]
- [[ XGBoost]]

---
tags: #timeseriesdata, #timeseriesdata/facebookprophet
