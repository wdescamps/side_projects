#  Random Forests
**Model Type:**  Classification Models
**Data Type:**  Numerical Data

**Python code **:


```python
# Importing libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the iris dataset
data = load_iris()
features = data.data
target = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

# Create a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
predictions = clf.predict(X_test)

# Calculate accuracy and display the classification report
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Classification Report:\n", classification_report(y_test, predictions))
```

This code demonstrates the use of the Random Forest classification model to predict iris species using the famous iris dataset. The RandomForestClassifier from scikit-learn is imported and used to fit the model on the training data, make predictions on the test data, and evaluate the model's accuracy.


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
- [[ Support Vector Machines (SVM)]]
- [[ Decision Trees]]
- [[ Naive Bayes]]
- [[ k]]
- [[ AdaBoost]]
- [[ Gradient Boosting Machines (GBM)]]
- [[ XGBoost]]
- [[ LightGBM]]
- [[ CatBoost]]
## Resources

a. Scikit-Learn documentation: Random Forests is implemented in Python's scikit-learn library, which provides comprehensive documentation and examples.
Link: https://scikit-learn.org/stable/modules/ensemble.html#forest
b. DataCamp tutorial on Random Forests:
This tutorial offers a step-by-step instruction for implementing Random Forests in Python, covering both classification and regression problems.
Link: https://www.datacamp.com/community/tutorials/random-forests-classifier-python
c. Towards Data Science article on Random Forests:
This article provides an introduction to Random Forests, its advantages, and disadvantages while explaining its implementation in Python.
Link: https://towardsdatascience.com/understanding-random-forest-58381e0602d2


---
tags: #-numerical-data, #-numerical-data/-random-forests
