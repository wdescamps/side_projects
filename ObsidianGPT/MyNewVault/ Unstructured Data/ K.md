**Model Type:**  Clustering Models
**Data Type:**  Unstructured Data

## Use Cases :

a) Image recognition: KNN can be used for tasks such as image classification and character recognition, by comparing pixel values of an image with K nearest neighbors in the dataset.

b) Recommender systems: KNN can be used to create recommender systems that suggest similar items to users based on their preferences, by finding K nearest neighbors with the highest similarity to the target item or user.

c) Anomaly detection: KNN can be employed to identify unusual data points, by checking whether they have relatively fewer close neighbors compared to the rest of the dataset.


## Python code: 

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Create KNN classifier with k=3
knn = KNeighborsClassifier(n_neighbors=3)

# Fit the model to the training data
knn.fit(X_train, y_train)

# Predict labels for the test data
y_pred = knn.predict(X_test)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
```

This Python code demonstrates the use of the KNN model using Scikit-learn library for the famous Iris dataset. The KNN classifier is created with K=3, and the model is trained and evaluated using confusion matrix and classification report.


## Resources

a) Scikit-learn documentation on K Nearest Neighbors: https://scikit-learn.org/stable/modules/neighbors.html
This is the official documentation of the popular Python library Scikit-learn, which provides a comprehensive explanation of the KNN algorithm and practical implementation instructions.
b) KNN tutorial by Sentdex on YouTube: https://www.youtube.com/watch?v=44jq6ano5n0
A video tutorial by Sentdex that shows how to implement KNN from scratch using Python and demonstrates how to apply it to a real-life dataset.
c) KNN classification tutorial by Machine Learning Mastery: https://machinelearningmastery.com/tutorial-k-nearest-neighbors-in-python/
A step-by-step tutorial with Python code examples that guide you through the implementation of KNN classification using Scikit-learn library.

**See Also**:

- [[ DBSCAN]]
- [[ Hierarchical Clustering]]
- [[ Mean Shift]]
- [[ Principal Component Analysis (PCA)]]
- [[ Linear Discriminant Analysis (LDA)]]
- [[ t]]
- [[ Uniform Manifold Approximation and Projection (UMAP)]]
- [[ Autoencoders]]

---
tags: #unstructureddata, #unstructureddata/k
