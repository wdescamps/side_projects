#  k
**Model Type:**  Classification Models
**Data Type:**  Numerical Data

**Python code **:


```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generate sample data
data, _ = make_blobs(n_samples=300, centers=3, random_state=42, cluster_std=1.5)

# Create and fit the k-means model
kmeans = KMeans(n_clusters=3, random_state=42).fit(data)

# Predict the cluster labels for each data point
labels = kmeans.predict(data)

# Plot the data points and cluster centroids
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=100)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-means Clustering')
plt.show()
```

This code generates a dataset of 300 points in 2D, with three distinct clusters. It then applies the k-means algorithm with k=3 to fit the data and predict the cluster labels. Finally, it plots the data points and cluster centroids to visualize the clustering results.


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
- [[ Random Forests]]
- [[ Naive Bayes]]
- [[ AdaBoost]]
- [[ Gradient Boosting Machines (GBM)]]
- [[ XGBoost]]
- [[ LightGBM]]
- [[ CatBoost]]
## Resources

i. Scikit-learn k-means clustering documentation: This official documentation provides a detailed description and implementation of the k-means clustering algorithm using the Scikit-learn library in Python. (https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
ii. K-means tutorial from Scratch: This tutorial explains how to implement the k-means algorithm from scratch in Python using NumPy. (https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/)
iii. K-means Clustering with TensorFlow: This tutorial demonstrates how to implement k-means clustering using TensorFlow, a powerful machine learning library. (https://www.tensorflow.org/addons/tutorials/networks_dynamic_clustering)


---
tags: #-numerical-data, #-numerical-data/-k
