#  LightGBM
**Model Type:**  Exponential Smoothing State Space Models (ETS)
**Data Type:**  Time Series Data

**Python code **:


```python
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert data into LightGBM Dataset format
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

# Define the parameters of the LightGBM model
params = {
    'boosting_type': 'gbdt',
    'objective': 'multiclass',
    'num_class': 3,
    'metric': 'multi_logloss',
    'feature_fraction': 0.8,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'learning_rate': 0.1,
    'num_iterations': 100,
    'verbose': -1
}

# Train the LightGBM model
model = lgb.train(params, train_data, valid_sets=test_data, early_stopping_rounds=10)

# Make predictions using the trained model
y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=1) # Get the index (class) with the highest probability

# Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
```

This example demonstrates the use of LightGBM for a multiclass classification task on the Iris dataset. It imports the necessary libraries, loads the data, and splits it into training and testing sets. The data is then converted into the LightGBM Dataset format, and parameters for the model are defined. After training, the model is applied to make predictions on the test set, and its accuracy is evaluated.


**See Also**:

- [[ Autoregressive Integrated Moving Average (ARIMA)]]
- [[ Seasonal decomposition of time series (STL)]]
- [[ Recurrent Neural Networks (RNN)]]
- [[ Long Short]]
- [[ Gated Recurrent Units (GRU)]]
- [[ Facebook Prophet]]
- [[ XGBoost]]
## Resources

a. Official LightGBM GitHub repository: https://github.com/microsoft/LightGBM
This repository contains the source code, documentation, examples, and development resources needed to implement LightGBM in your projects.
b. LightGBM Python API Documentation: https://lightgbm.readthedocs.io/en/latest/Python-API.html
This comprehensive documentation provides an outline of the Python API and detailed information on how to use LightGBM in Python.
c. A Gentle Introduction to LightGBM for Applied Machine Learning: https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/
This article provides a thorough introduction to the LightGBM model, explaining key concepts, techniques used, and practical guidance on how to employ it in machine learning tasks.


---
tags: #-time-series-data, #-time-series-data/-lightgbm
