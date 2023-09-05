**Model Type:**  Dimensionality Reduction Models
**Data Type:**  Unstructured Data

## Use Cases :

a. Hypothesis testing: The t-distribution is used in the Student's t-test to determine if there is a significant difference between two independent sample means.

b. Confidence intervals: It's used to construct confidence intervals for small samples, specifically when the population variance is unknown.

c. Regression analysis: The t-distribution helps assess the statistical significance of regression coefficients in linear regression models when sample sizes are small or population variances are unknown.


## Python code: 

```python
import numpy as np
import pandas as pd
import scipy.stats as stats

# Example: Independent two-sample t-test to determine if there's a significant difference between two datasets
data1 = [6.2, 5.8, 7.5, 8.0, 6.5]
data2 = [5.0, 4.8, 5.7, 4.9, 6.0]

# Calculate t-statistic and p-value
t_stat, p_value = stats.ttest_ind(data1, data2)

print("t-statistic:", t_stat)
print("p-value:", p_value)

# Example: Calculating the t-distribution probability density function at x = 2 with 10 degrees of freedom
x = 2
df = 10
prob_density = stats.t.pdf(x, df)
print("Probability Density Function:", prob_density)

# Example: Finding the critical value for a 95% confidence interval with 10 degrees of freedom
conf_interval = 0.95
critical_value = stats.t.ppf((1 + conf_interval) / 2, df)
print("Critical Value:", critical_value)
```


## Resources

a. An Overview of the T Distribution (Stat Trek, Online Tutorial): [https://stattrek.com/probability-distributions/t-distribution.aspx](https://stattrek.com/probability-distributions/t-distribution.aspx)
b. Student’s t-Distribution (Wikipedia): [https://en.wikipedia.org/wiki/Student%27s_t-distribution](https://en.wikipedia.org/wiki/Student%27s_t-distribution)
c. Introduction to the t Distributions (Math Is Fun): [https://www.mathsisfun.com/data/t-distribution.html](https://www.mathsisfun.com/data/t-distribution.html)

**See Also**:

- [[ K]]
- [[ DBSCAN]]
- [[ Hierarchical Clustering]]
- [[ Mean Shift]]
- [[ Principal Component Analysis (PCA)]]
- [[ Linear Discriminant Analysis (LDA)]]
- [[ Uniform Manifold Approximation and Projection (UMAP)]]
- [[ Autoencoders]]

---
tags: #unstructureddata, #unstructureddata/t
