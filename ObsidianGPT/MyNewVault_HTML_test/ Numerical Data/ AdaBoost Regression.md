**Model Type:**  Regression Models
**Data Type:**  Numerical Data

## Use Cases :


## Python code: 
```python
# Import required libraries
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import load_boston

# Load the Boston House prices dataset
data = load_boston()
X, y = data.data, data.target

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize AdaBoostRegressor with 100 base decision trees
regressor = AdaBoostRegressor(n_estimators=100, random_state=42)

# Train the AdaBoostRegressor on the training data
regressor.fit(X_train, y_train)

# Make predictions on the test data
y_pred = regressor.predict(X_test)

# Calculate the Mean Squared Error and the R-squared score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the results
print("Mean Squared Error:", mse)
print("R-squared Score:", r2)
```

This code implements AdaBoost Regression on the Boston House Prices dataset using sklearn's AdaBoostRegressor. It prints the Mean Squared Error and R-squared score to evaluate the performance of the model.


## Resources


**See Also**:

- [[ Linear Regression]]
- [[ Lasso Regression]]
- [[ Ridge Regression]]
- [[ Elastic Net]]
- [[ Support Vector Regression (SVR)]]
- [[ Decision Tree Regression]]
- [[ Random Forest Regression]]
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
tags: #numericaldata, #numericaldata/adaboostregression
