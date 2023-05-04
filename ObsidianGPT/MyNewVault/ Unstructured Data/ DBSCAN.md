#  DBSCAN
**Model Type:**  Clustering Models
**Data Type:**  Unstructured Data

**Python code **:


```python
# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN

# Generating random sample dataset
data, labels = make_blobs(n_samples=300, centers=4, random_state=42)

# Displaying the generated dataset
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.title("Generated Dataset")
plt.show()

# Applying DBSCAN model
dbscan = DBSCAN(eps=1, min_samples=5)
dbscan.fit(data)

# Visualizing the results
plt.scatter(data[:, 0], data[:, 1], c=dbscan.labels_, cmap='viridis')
plt.title("DBSCAN Clustering")
plt.show()
```

This code creates a dataset with four clusters and then applies the DBSCAN algorithm to identify these clusters. The original dataset and the clustering result are visualized using Matplotlib.


**See Also**:

- [[ K]]
- [[ Hierarchical Clustering]]
- [[ Mean Shift]]
- [[ Principal Component Analysis (PCA)]]
- [[ Linear Discriminant Analysis (LDA)]]
- [[ t]]
- [[ Uniform Manifold Approximation and Projection (UMAP)]]
- [[ Autoencoders]]
## Resources

a. DBSCAN: A Macroscopic Investigation in Python
(https://towardsdatascience.com/dbscan-a-macroscopic-investigation-in-python-5d5577d88dcd)
b. Scikit-Learn - DBSCAN Clustering
(https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)
c. Introduction to Density-Based Clustering Algorithms with Python
(https://realpython.com/density-based-clustering-dbscan-python/)


---
tags: #-unstructured-data, #-unstructured-data/-dbscan
