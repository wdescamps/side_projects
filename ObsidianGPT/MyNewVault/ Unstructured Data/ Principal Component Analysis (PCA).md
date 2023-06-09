**Model Type:**  Dimensionality Reduction Models
**Data Type:**  Unstructured Data

## Use Cases :

a. Data Visualization: PCA can be used to reduce high-dimensional data to 2 or 3 dimensions, allowing for easier visualization and understanding of underlying patterns or relationships.

b. Noise Reduction: PCA can help remove noise from data by keeping only the components with the highest variance, effectively filtering out insignificant variations.

c. Feature Engineering: PCA can be used as a preprocessing step in machine learning pipelines for feature extraction and dimensionality reduction, which improves the efficiency and performance of the model.


## Python code: 

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Apply PCA to reduce the number of features to 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot the 2D transformed dataset
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA applied to the Iris Dataset')
plt.show()
```

This short script applies PCA to the Iris dataset, originally containing four features, and reduces it to two dimensions. The 2D transformed dataset is then plotted, showing the distinct separation between the three classes of flowers.


## Resources

a. Scikit-learn Documentation: A comprehensive guide and implementation of PCA using the scikit-learn library in Python. (https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
b. An Introduction to PCA: This tutorial on Towards Data Science provides a lucid introduction to PCA along with examples in Python. (https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c)
c. Eigenvectors, Eigenvalues and PCA: A video lecture from Professor Gilbert Strang that explains the mathematical concepts behind PCA, such as eigenvectors and eigenvalues. (https://www.youtube.com/watch?v=uqZi3HGq3Vs)

**See Also**:

- [[ K]]
- [[ DBSCAN]]
- [[ Hierarchical Clustering]]
- [[ Mean Shift]]
- [[ Linear Discriminant Analysis (LDA)]]
- [[ t]]
- [[ Uniform Manifold Approximation and Projection (UMAP)]]
- [[ Autoencoders]]

---
tags: #unstructureddata, #unstructureddata/principalcomponentanalysispca
