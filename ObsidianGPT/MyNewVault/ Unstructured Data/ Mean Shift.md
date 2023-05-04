#  Mean Shift
**Model Type:**  Clustering Models
**Data Type:**  Unstructured Data

**Python code **:


```python
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt

# Create a toy dataset with 3 clusters
X, y = make_blobs(n_samples=300, centers=3, cluster_std=0.8, random_state=0)

# Apply Mean Shift clustering
ms = MeanShift()
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

# Calculate the number of clusters
n_clusters = len(np.unique(labels))
print("Number of estimated clusters:", n_clusters)

# Plot the clustering result
colors = ['r', 'g', 'b']
for i in range(n_clusters):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], c=colors[i], label=f'Cluster {i}')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='k', marker='x', label='Centroids')
plt.legend()
plt.title("Mean Shift Clustering")
plt.show()
```

This code snippet generates a toy dataset with three clusters, applies the Mean Shift algorithm to find the clusters, and plots the clustering result.


**See Also**:

- [[ K]]
- [[ DBSCAN]]
- [[ Hierarchical Clustering]]
- [[ Principal Component Analysis (PCA)]]
- [[ Linear Discriminant Analysis (LDA)]]
- [[ t]]
- [[ Uniform Manifold Approximation and Projection (UMAP)]]
- [[ Autoencoders]]
## Resources

a. Scikit-learn's MeanShift documentation provides a comprehensive guide on how to use Mean Shift for clustering tasks in Python: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html
b. This tutorial by PyImageSearch covers how to use Mean Shift for object tracking in videos: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
c. This research paper provides an in-depth explanation of the Mean Shift algorithm, its properties, and applications: https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/TUZEL1/MeanShift.pdf


---
tags: #-unstructured-data, #-unstructured-data/-mean-shift
