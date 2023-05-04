#  Lasso Regression
**Model Type:**  Regression Models
**Data Type:**  Numerical Data

**Python code **:


```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

# Creating a sample dataset
data = {
    "x1": [1, 2, 3, 4, 5],
    "x2": [2, 4, 6, 8, 10],
    "y": [2, 3, 4, 5, 6],
}
df = pd.DataFrame(data)

# Defining the features and target variable
X = df[["x1", "x2"]]
y = df["y"]

# Splitting the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Applying Lasso Regression
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# Making predictions
y_pred = lasso.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
```

In this example, the Lasso Regression model is applied to a simple dataset with two features and evaluated using the mean squared error metric.


**See Also**:

- [[ Linear Regression]]
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
## Resources

a. Scikit-learn Documentation: Lasso Regression
(Link: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html)
b. An Introduction to Lasso Regression in Python by Analytics Vidhya
(Link: https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/)
c. Lasso Regression using Python - A Step by Step tutorial by DataCamp
(Link: https://www.datacamp.com/community/tutorials/tutorial-ridge-lasso-elastic-net)


---
tags: #-numerical-data, #-numerical-data/-lasso-regression
