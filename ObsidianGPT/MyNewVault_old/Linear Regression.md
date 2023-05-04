**Model Type**: Regression

**Data Type**: Numerical

**Python code **:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate synthetic data
X = np.random.rand(100, 1) * 10
y = 3 * X + 5 + np.random.randn(100, 1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Check the prediction accuracy by calculating the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean squared error: ", mse)

# Visualize the fitted line
plt.scatter(X, y, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.xlabel('Input feature')
plt.ylabel('Target variable')
plt.show()
```
This Python code demonstrates the use of the Scikit-learn library to create a synthetic dataset, split the data into training and testing sets, fit a Linear Regression model, and visualize the results.


**See Also**:

- [[Ridge Regression]]
- [[Lasso Regression]]
- [[Elastic Net]]
- [[Support Vector Machines (for regression)]]
- [[Decision Trees (for regression)]]
- [[Random Forest (for regression)]]
- [[Gradient Boosting Machines (for regression)]]
- [[XGBoost (for regression)]]
- [[Artificial Neural Networks (for regression)]]
- [[Logistic Regression]]
- [[Naive Bayes Classifier]]
- [[K-Nearest Neighbors]]
- [[Support Vector Machines (for classification)]]
- [[Decision Trees (for classification)]]
- [[Random Forest (for classification)]]
- [[Gradient Boosting Machines (for classification)]]
- [[XGBoost (for classification)]]
- [[AdaBoost]]
- [[CatBoost]]
- [[LightGBM]]
- [[Artificial Neural Networks (for classification)]]
**Python Resources**:

['a. Scikit-learn tutorial on Linear Regression: https://scikit-learn.org/stable/modules/linear_model.html', 'b. A comprehensive guide to Linear Regression in Python: https://realpython.com/linear-regression-in-python/', 'c. A step-by-step guide to implementing Linear Regression from scratch: https://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/']


---
tags: #numerical, #numerical/linear-regression
