#  Hierarchical Clustering
**Model Type:**  Clustering Models
**Data Type:**  Unstructured Data

**Python code **:


```python
import numpy as np
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

# Generate random data points
data, labels = make_blobs(n_samples=200, centers=3, random_state=42)

# Perform hierarchical clustering using ward linkage method
linkage_matrix = linkage(data, method='ward')

# Visualize the dendrogram
dendrogram(linkage_matrix)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Euclidean Distance')
plt.show()

# Apply the agglomerative clustering algorithm
num_clusters = 3
model = AgglomerativeClustering(n_clusters=num_clusters, affinity='euclidean', linkage='ward')
predicted_labels = model.fit_predict(data)

# Plot the clusters
for i in range(0, num_clusters):
    cluster = data[predicted_labels == i]
    plt.scatter(cluster[:, 0], cluster[:, 1], label=f"Cluster {i}")

plt.legend()
plt.title('Hierarchical Clustering Result')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```

This Python code demonstrates how to use the Hierarchical Clustering model with the help of the Scipy and Scikit-learn libraries. It generates random data points using the make_blobs function, performs hierarchical clustering using the ward linkage method, and visualizes the dendrogram. Then, it applies the agglomerative clustering algorithm to cluster the data points into three clusters and plots the result.


**See Also**:

- [[ K]]
- [[ DBSCAN]]
- [[ Mean Shift]]
- [[ Principal Component Analysis (PCA)]]
- [[ Linear Discriminant Analysis (LDA)]]
- [[ t]]
- [[ Uniform Manifold Approximation and Projection (UMAP)]]
- [[ Autoencoders]]
## Resources

a. Scikit-learn User Guide on Hierarchical Clustering:
https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering
b. A Comprehensive Guide to Hierarchical Clustering in Python by Analytics Vidhya:
https://www.analyticsvidhya.com/blog/2019/05/beginners-guide-hierarchical-clustering/
c. Hierarchical Clustering in Python with an Example by Machine Learning Mastery:
https://machinelearningmastery.com/hierarchical-clustering-with-python-and-scikit-learn/


---
tags: #-unstructured-data, #-unstructured-data/-hierarchical-clustering
