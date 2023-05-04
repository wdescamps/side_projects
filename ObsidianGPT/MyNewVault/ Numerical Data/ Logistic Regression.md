**Model Type:**  Classification Models
**Data Type:**  Numerical Data

## Use Cases :

a. Medical Diagnosis: Logistic regression can be used to predict the likelihood of a patient having a particular disease given certain symptoms or test results.

b. Spam Detection: The model can be utilized to classify emails into spam and non-spam categories based on the presence of certain keywords or patterns.

c. Credit Risk Analysis: Logistic regression can help assess the probability of a borrower defaulting on a loan based on factors such as income, credit score, and loan amount.


## Python code: 

```python
# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Random dataset for demonstration
data = pd.DataFrame({'X1': np.random.rand(100), 'X2': np.random.rand(100)})
data['Y'] = np.round(data['X1'] + data['X2'])

# Splitting the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(data[['X1', 'X2']], data['Y'], test_size=0.3)

# Creating and training the logistic regression model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Making predictions on the test set
Y_pred = model.predict(X_test)

# Evaluating the model's performance
accuracy = accuracy_score(Y_test, Y_pred)
conf_matrix = confusion_matrix(Y_test, Y_pred)
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
```

The above code demonstrates how to implement logistic regression using Scikit-learn on a sample dataset. After creating the dataset, it is split into training and testing sets. A logistic regression model is then created and trained on the training set, tested on the test set, and evaluated using accuracy and confusion matrix metrics.


## Resources

a. Scikit-learn Documentation: A widely used Python library for machine learning, the logistic regression implementation in Scikit-learn is easy to use and comes with comprehensive documentation.
Link: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
b. Coursera Course (Machine Learning by Andrew Ng): This course provides a deep understanding of logistic regression, including the math behind the model and how it can be implemented.
Link: https://www.coursera.org/learn/machine-learning
c. Towards Data Science Article: This article explains the intuition behind logistic regression and provides an example of how to implement the model using Python and Scikit-learn.
Link: https://towardsdatascience.com/logistic-regression-a-simplified-approach-using-python-c4bc81a87c31

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
tags: #numericaldata, #numericaldata/logisticregression
