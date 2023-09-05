**Model Type:**  Regression Models
**Data Type:**  Numerical Data

## Use Cases :

a. Sales Forecasting: Linear regression can be used to predict future sales based on historical data, such as advertising spend, customer demographics, or seasonality.

b. Pricing Optimization: Businesses can use linear regression to understand how price changes impact demand and optimize the pricing strategy accordingly.

c. Risk Assessment: Linear regression can help evaluate risk factors in finance, insurance, or healthcare industries, where understanding the relationships between different factors is crucial for decision-making.


## Python code: 
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset - dependent variable (y) and independent variable (x)
x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([2, 5, 6, 9, 12, 15])

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create a Linear Regression Model
model = LinearRegression()

# Train the model with the training dataset
model.fit(x_train, y_train)

# Make predictions using the testing dataset
y_pred = model.predict(x_test)

# Evaluate the model performance
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean squared error (MSE): %.2f" % mean_squared_error(y_test, y_pred))
print("Coefficient of determination (R^2): %.2f" % r2_score(y_test, y_pred))

# Visualize the results
plt.scatter(x_test, y_test, color='black')
plt.plot(x_test, y_pred, color='blue', linewidth=2)
plt.xlabel('X (Independent Variable)')
plt.ylabel('Y (Dependent Variable)')
plt.title('Linear Regression Example')
plt.show()
```
This code demonstrates how to create and evaluate a Linear Regression model using Python's Scikit-learn library, using a simple example dataset. The code generates a plot of the resulting regression line alongside the dependent variable.


## Resources

a. Scikit-Learn Documentation for Linear Regression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
b. Linear Regression in Python - An Introduction: https://realpython.com/linear-regression-in-python/
c. Coursera Machine Learning Course (by Andrew Ng) - Linear Regression Module: https://www.coursera.org/lecture/machine-learning/model-representation-db3jS

**See Also**:

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
- [[ Gradient Boosting Machines (GBM)]]
- [[ XGBoost]]
- [[ LightGBM]]
- [[ CatBoost]]

---
tags: #numericaldata, #numericaldata/linearregression
