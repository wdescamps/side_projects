**Model Type**: Regression

**Data Type**: Numerical

**Python code **:


```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

# Load the Boston Housing dataset
boston_dataset = load_boston()
data = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
target = pd.Series(boston_dataset.target, name="Price")

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=42)

# Create and fit the Lasso Regression model
lasso = Lasso(alpha=0.5)
lasso.fit(X_train, y_train)

# Perform predictions using the model
y_train_pred = lasso.predict(X_train)
y_test_pred = lasso.predict(X_test)

# Calculate and display the Mean Squared Error
mse_train = mean_squared_error(y_train, y_train_pred)
mse_test = mean_squared_error(y_test, y_test_pred)

print(f"Mean Squared Error (Train): {mse_train:.2f}")
print(f"Mean Squared Error (Test): {mse_test:.2f}")

# Display coefficient values for each feature
print("\nFeature Coefficients")
for feature, coef in zip(boston_dataset.feature_names, lasso.coef_):
    print(f"{feature}: {coef:.2f}")
```

This code demonstrates how to implement Lasso Regression in Python using the scikit-learn library. It first loads the Boston Housing dataset and splits it into training and testing data. The Lasso Regression model is then created, fit, and used for prediction. The Mean Squared Error (MSE) is calculated and displayed for both the training and testing data, and the model's feature coefficients are printed.


**See Also**:

- [[Linear Regression]]
- [[Ridge Regression]]
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

['- Scikit-learn Lasso Regression documentation: A detailed explanation and implementation guide for Lasso Regression in Python utilizing the well-known scikit-learn library.', 'https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html', '- Introduction to Lasso Regression: A comprehensive blog post explaining Lasso Regression theory, implementation, and applications.', 'https://towardsdatascience.com/regularization-in-machine-learning-connecting-the-dots-c6e030bfaddd', '- Machine Learning Mastery - Lasso Regression with Python: A tutorial to understand Lasso Regression and implement it using Python.', 'https://machinelearningmastery.com/lasso-regression-with-python/']


---
tags: #numerical, #numerical/lasso-regression
