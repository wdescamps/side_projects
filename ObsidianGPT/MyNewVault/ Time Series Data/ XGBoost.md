#  XGBoost
**Model Type:**  Exponential Smoothing State Space Models (ETS)
**Data Type:**  Time Series Data

**Python code **:


```python
# Import necessary libraries
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate an XGBoost classifier
xgboost_classifier = xgb.XGBClassifier()

# Fit the classifier to the training data
xgboost_classifier.fit(X_train, y_train)

# Make predictions on test data
y_pred = xgboost_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
```

This example demonstrates how to use XGBoost in Python for a simple multi-class classification problem, using the Iris dataset. The code imports necessary libraries, loads the dataset, splits it into training and testing sets, creates an XGBoost classifier, fits it to the data, makes predictions, and calculates the accuracy of the model.


**See Also**:

- [[ Autoregressive Integrated Moving Average (ARIMA)]]
- [[ Seasonal decomposition of time series (STL)]]
- [[ Recurrent Neural Networks (RNN)]]
- [[ Long Short]]
- [[ Gated Recurrent Units (GRU)]]
- [[ Facebook Prophet]]
- [[ LightGBM]]
## Resources

a. XGBoost Official Documentation: This is the principal resource for understanding the algorithm and its usage for different machine learning tasks: https://xgboost.readthedocs.io/en/latest/
b. "A Complete Guide to XGBoost Model in Python Using scikit-learn" by Manish Pathak: This practical guide provides a step-by-step procedure to implement XGBoost in Python: https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/
c. "Hands-On Gradient Boosting with XGBoost and scikit-learn" (Book) by Sagi Shaier: This book covers essential techniques for gradient boosting with XGBoost and scikit-learn, including practical code examples: https://www.amazon.com/Hands-Gradient-Boosting-XGBoost-scikit-learn/dp/1801073208


---
tags: #-time-series-data, #-time-series-data/-xgboost
