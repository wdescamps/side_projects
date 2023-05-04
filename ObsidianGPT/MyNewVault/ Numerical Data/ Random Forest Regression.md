**Model Type:**  Regression Models
**Data Type:**  Numerical Data

## Use Cases :

a. Real estate pricing: Predicting house prices based on various features like location, square footage, year built, amenities, etc.

b. Stock market prediction: Predicting stock prices based on historical data, technical indicators, and market sentiment.

c. Demand forecasting: Predicting the demand for a product in the future based on historical sales data, seasonality, and other external factors.


## Python code: 

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
dataset = load_boston()
data, target = dataset.data, dataset.target

# Create a DataFrame
data_frame = pd.DataFrame(data, columns=dataset.feature_names)
data_frame['PRICE'] = target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data_frame.drop('PRICE', axis=1), data_frame['PRICE'], test_size=0.3, random_state=0)

# Create the RandomForestRegressor model
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=0)

# Train the model
rf_regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_regressor.predict(X_test)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print Metrics
print("Mean Squared Error: ", mse)
print("R-squared: ", r2)

```

This code demonstrates how to use the RandomForestRegressor from the Scikit-Learn library to predict housing prices in the well-known Boston Housing dataset. The code includes importing the necessary libraries, loading and preparing the dataset, creating and training the model, making predictions, and evaluating the model's performance using mean squared error and R-squared metrics.


## Resources

a. A Gentle Introduction to Random Forest for Regression - https://machinelearningmastery.com/random-forest-for-regression/
b. How to run Random Forest Regression in Python - https://towardsdatascience.com/random-forest-in-python-24d0893d51c0
c. Scikit-Learn Random Forest Regression Documentation - https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html

**See Also**:

- [[ Linear Regression]]
- [[ Lasso Regression]]
- [[ Ridge Regression]]
- [[ Elastic Net]]
- [[ Support Vector Regression (SVR)]]
- [[ Decision Tree Regression]]
- [[ AdaBoost Regression]]
- [[ Gradient Boosting Regression]]
- [[ XGBoost]]
- [[ LightGBM]]
- [[ CatBoost]]
- [[ Logistic Regression]]
- [[ Support Vector Machines (SVM)]]
- [[ Decision Trees]]
- [[ Random Forests]]
- [[ Naive Bayes]]
- [[ k]]
- [[ AdaBoost]]
- [[ Gradient Boosting Machines (GBM)]]
- [[ XGBoost]]
- [[ LightGBM]]
- [[ CatBoost]]

---
tags: #numericaldata, #numericaldata/randomforestregression
