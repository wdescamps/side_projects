**Model Type:**  Classification Models
**Data Type:**  Numerical Data

## Use Cases :

a. Predictive Analytics: GBM can be used to predict outcomes, such as customer likelihood for churn or credit default, based on historical data with multiple features.

b. Regression: GBM can be used to solve regression problems like predicting housing prices, sales forecasting, or energy usage.

c. Classification: GBM can be used to solve binary or multiclass classification problems, such as image recognition, natural language processing, or fraud detection.


## Python code: 

```python
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Load the Boston house prices dataset (a regression dataset)
dataset = load_boston()
X = dataset.data
y = dataset.target

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a GradientBoostingRegressor model
gbm = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gbm.fit(X_train, y_train)

# Make predictions on the test set
y_pred = gbm.predict(X_test)

# Compute the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error: ", mse)
```
This code demonstrates how to train a GBM regression model using the GradientBoostingRegressor from Scikit-Learn. The toy dataset used here is the Boston Housing dataset, which is a standard regression problem. The trained model predicts house prices based on several features and evaluates the performance using the mean squared error metric.


## Resources

a. Hands-on Gradient Boosting with XGBoost and scikit-learn: This tutorial explains the inner workings of GBM and demonstrates how to work with the gradient boosting algorithm in Python using the XGBoost library and scikit-learn.
Link: https://www.datacamp.com/community/tutorials/xgboost-in-python
b. Gentle Introduction to the Gradient Boosting Algorithm for Machine Learning: This article introduces the gradient boosting method for machine learning and gives an overview of its application and benefits.
Link: https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/
c. Official documentation for LightGBM: LightGBM is a gradient boosting framework that uses tree-based algorithms and provides faster training speeds and better efficiency. This is the official guide for LightGBM with examples and API references.
Link: https://lightgbm.readthedocs.io/en/latest/

**See Also**:

- [[ Linear Regression]]
- [[ Lasso Regression]]
- [[ Ridge Regression]]
- [[ Elastic Net]]
- [[ Support Vector Regression (SVR)]]
- [[ Decision Tree Regression]]
- [[ Random Forest Regression]]
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
- [[ XGBoost]]
- [[ LightGBM]]
- [[ CatBoost]]

---
tags: #numericaldata, #numericaldata/gradientboostingmachinesgbm
