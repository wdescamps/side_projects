#  LightGBM
**Model Type:**  Classification Models
**Data Type:**  Numerical Data

**Python code **:


```python
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score

# Load the dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert the data into LightGBM dataset format
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test)

# Set the parameters for the LightGBM model
params = {
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': 'binary_logloss',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9
}

# Train the LightGBM model
model = lgb.train(params, train_data, num_boost_round=100,
                  valid_sets=[train_data, test_data], early_stopping_rounds=10, verbose_eval=10)

# Make predictions using the trained model
y_pred = model.predict(X_test, num_iteration=model.best_iteration)
y_pred = np.round(y_pred)  # Convert probabilities to binary values

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of the LightGBM model: {:.2f}".format(accuracy))
```
This code demonstrates training a LightGBM model on the breast cancer dataset and evaluating its accuracy on the test data.


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
- [[ CatBoost]]
## Resources

a. Official LightGBM GitHub Repository: This repository contains the source code, documentation, and examples for LightGBM. It is an excellent starting point for anyone looking to implement the model.
Link: https://github.com/microsoft/LightGBM
b. LightGBM Python Package: This Python package provides an easy-to-use API for training and using LightGBM models in Python.
Link: https://pypi.org/project/lightgbm/
c. A Gentle Introduction to LightGBM for Applied Machine Learning: This blog post offers a clear and concise introduction to LightGBM, including its features and working principles.
Link: https://machinelearningmastery.com/gentle-introduction-lightgbm-applied-machine-learning/


---
tags: #-numerical-data, #-numerical-data/-lightgbm
