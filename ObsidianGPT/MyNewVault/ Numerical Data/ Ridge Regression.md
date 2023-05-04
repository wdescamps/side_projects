#  Ridge Regression
**Model Type:**  Regression Models
**Data Type:**  Numerical Data

**Python code **:


```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# Generate synthetic data for demonstration
np.random.seed(0)
X = np.random.rand(100, 3)
y = 5 * X[:, 0] - 3 * X[:, 1] + 2 * X[:, 2] + np.random.normal(0, 0.5, size=100)

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Ridge Regression model
alpha = 0.1  # Regularization parameter
ridge_model = Ridge(alpha=alpha)
ridge_model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = ridge_model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Print the learned coefficients
print("Coefficients:", ridge_model.coef_)
```

This code snippet generates synthetic data, splits it into training and testing sets, trains a Ridge Regression model, performs predictions and evaluates the performance, and finally prints the learned coefficients.


**See Also**:

- [[ Linear Regression]]
- [[ Lasso Regression]]
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
## Resources

a) Ridge Regression in scikit-learn: https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression
b) Ridge Regression tutorial by Analytics Vidhya: https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/
c) Ridge Regression explained by StatQuest: https://www.youtube.com/watch?v=Q81RR3yKn30


---
tags: #-numerical-data, #-numerical-data/-ridge-regression
