**Model Type:**  Regression Models
**Data Type:**  Numerical Data

## Use Cases :

a. Predicting Stock Prices: SVR can be used to model the relationship between various factors (e.g., historical prices, trading volume, market sentiment) and stock prices to make future price predictions.

b. Medical Diagnosis: SVR can be applied to predict health outcomes or progression of diseases based on patient data and clinical measurements.

c. Energy Consumption Forecasting: Utilities companies can use SVR to predict future energy consumption based on historical usage patterns, weather conditions, and demographic information, helping them better manage energy resources.


## Python code: 

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Create synthetic data
np.random.seed(42)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - np.random.rand(16))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit regression model
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_lin = SVR(kernel='linear', C=100, gamma='auto')
svr_poly = SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1, coef0=1)

# Train models using the training data
svr_rbf.fit(X_train, y_train)
svr_lin.fit(X_train, y_train)
svr_poly.fit(X_train, y_train)

# Make predictions using the testing data
y_pred_rbf = svr_rbf.predict(X_test)
y_pred_lin = svr_lin.predict(X_test)
y_pred_poly = svr_poly.predict(X_test)

# Evaluate the performance of the models
mse_rbf = mean_squared_error(y_test, y_pred_rbf)
mse_lin = mean_squared_error(y_test, y_pred_lin)
mse_poly = mean_squared_error(y_test, y_pred_poly)

r2_rbf = r2_score(y_test, y_pred_rbf)
r2_lin = r2_score(y_test, y_pred_lin)
r2_poly = r2_score(y_test, y_pred_poly)

print("Mean Squared Errors: RBF: {:.3f}, Linear: {:.3f}, Polynomial: {:.3f}".format(mse_rbf, mse_lin, mse_poly))
print("R-squared Scores: RBF: {:.3f}, Linear: {:.3f}, Polynomial: {:.3f}".format(r2_rbf, r2_lin, r2_poly))

# Plot the results
plt.scatter(X, y, c='k', label='data')
plt.plot(X_test, y_pred_rbf, c='g', label='RBF model')
plt.plot(X_test, y_pred_lin, c='r', label='Linear model')
plt.plot(X_test, y_pred_poly, c='b', label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
```


## Resources

a. Scikit-learn Documentation: Official documentation of the popular machine learning library scikit-learn includes a user guide and code examples for implementing SVR.
(https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html)
b. Support Vector Regression with R: A step-by-step tutorial on how to implement Support Vector Regression using R programming language.
(https://www.machinelearningplus.com/machine-learning/support-vector-regression-r/)
c. An Introduction to Support Vector Regression (SVR) in Python: A comprehensive article that provides an introduction to SVR, along with implementation details and code examples in Python.
(https://towardsdatascience.com/an-introduction-to-support-vector-regression-svr-a3ebc1672c2)

**See Also**:

- [[ Linear Regression]]
- [[ Lasso Regression]]
- [[ Ridge Regression]]
- [[ Elastic Net]]
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
tags: #numericaldata, #numericaldata/supportvectorregressionsvr
