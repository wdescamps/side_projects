#  Uniform Manifold Approximation and Projection (UMAP)
**Model Type:**  Dimensionality Reduction Models
**Data Type:**  Unstructured Data

**Python code **:


```python
import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import umap

# Load the sample dataset - Digits dataset from scikit-learn
data, labels = load_digits(return_X_y=True)

# Instantiate UMAP model
model = umap.UMAP(n_neighbors=15, min_dist=0.1, n_components=2, random_state=42)

# Fit the model and transform the data
reduced_data = model.fit_transform(data)

# Plot the reduced data
plt.figure(figsize=(12, 8))
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels, cmap='Spectral', s=5)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.title('UMAP projection of Digits dataset', fontsize=16)
plt.show()
```

This code demonstrates how to use UMAP to perform dimensionality reduction on the Digits dataset from scikit-learn, and then visualizes the resulting low-dimensional representation using a scatter plot.


**See Also**:

- [[ K]]
- [[ DBSCAN]]
- [[ Hierarchical Clustering]]
- [[ Mean Shift]]
- [[ Principal Component Analysis (PCA)]]
- [[ Linear Discriminant Analysis (LDA)]]
- [[ t]]
- [[ Autoencoders]]
## Resources

a. UMAP documentation - The official documentation for the UMAP Python library, with installation instructions, usage examples, and more: https://umap-learn.readthedocs.io/en/latest/
b. "How to Use UMAP" tutorial by Leland McInnes - A step-by-step tutorial on using UMAP for dimensionality reduction and data visualization by the creator of the UMAP algorithm: https://umap-learn.readthedocs.io/en/latest/basic_usage.html
c. UMAP GitHub repository - The official GitHub repository of the UMAP Python library, with source code, examples, and issues: https://github.com/lmcinnes/umap


---
tags: #-unstructured-data, #-unstructured-data/-uniform-manifold-approximation-and-projection-umap
