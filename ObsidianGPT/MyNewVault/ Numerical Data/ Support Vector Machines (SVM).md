#  Support Vector Machines (SVM)
**Model Type:**  Classification Models
**Data Type:**  Numerical Data

**Python code **:


```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

# Standardize the features
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Train the SVM model
svm = SVC(kernel='linear', C=1.0, random_state=1)
svm.fit(X_train_std, y_train)

# Make predictions
y_pred = svm.predict(X_test_std)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
```
In this example, we start by loading the iris dataset, extracting the petal length and width features, and splitting the data into training and testing sets. Once the data is prepared, we standardize the features using `StandardScaler`.

The SVM model is then instantiated and fit to the training data. After training, predictions are made on the test data, and the accuracy is calculated using the `accuracy_score` function from sklearn.metrics.


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
- [[ LightGBM]]
- [[ CatBoost]]
- [[ Logistic Regression]]
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

a. Scikit-learn's SVM Guide: https://scikit-learn.org/stable/modules/svm.html
b. Support Vector Machines: A Simple Explanation: https://towardsdatascience.com/support-vector-machines-a-simple-explanation-29aa4742406e
c. A Comprehensive Guide to Support Vector Machine (SVM): https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/


---
tags: #-numerical-data, #-numerical-data/-support-vector-machines-svm
