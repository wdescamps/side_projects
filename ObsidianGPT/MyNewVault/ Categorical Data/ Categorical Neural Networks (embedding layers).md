#  Categorical Neural Networks (embedding layers)
**Model Type:**  Classification Models
**Data Type:**  Categorical Data

**Python code **:


```python
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Sample dataset with categorical variable containing 6 categories represented as integers
data = np.array([[1], [2], [3], [4], [5], [6]])
labels = np.array([0, 1, 0, 1, 1, 0])

# Model configuration
embedding_dim = 3
num_categories = 6
output_dim = 1

# Building the model
model = models.Sequential([
    layers.Embedding(input_dim=num_categories+1, output_dim=embedding_dim, input_length=1),
    layers.Flatten(),
    layers.Dense(output_dim, activation='sigmoid')
])

# Compiling the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(data, labels, epochs=50, batch_size=2)

# Now you can use the model to make predictions, evaluate performance, and extract embeddings.
```

In this example, we create a simple neural network with an embedding layer to handle a categorical variable having 6 different categories (represented as integers from 1 to 6). We build a model using TensorFlow's Keras API, train it with a binary_crossentropy loss for predicting binary labels, and compile it with the Adam optimizer. Finally, we train the model on sample data for 50 epochs with a batch size of 2.


**See Also**:

- [[ Same as numerical classification models, as categorical data can be processed by encoding it into numerical representations.]]
- [[ Categorical Naive Bayes]]
## Resources

a. TensorFlow Embedding tutorial: This tutorial provides an introduction to embeddings and demonstrates how to create, train, and visualize embeddings using TensorFlow.
Link: https://www.tensorflow.org/tutorials/text/word_embeddings
b. PyTorch Embedding documentation: The official PyTorch documentation page for the Embedding layer provides explanations, code examples, and parameters for using embeddings in PyTorch.
Link: https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html
c. Neural Network Embeddings Explained: This blog post by Thushan Ganegedara gives a comprehensive overview of embeddings, their applications, and how to build an embedding layer in TensorFlow.
Link: https://towardsdatascience.com/neural-network-embeddings-explained-4d028e6f0526


---
tags: #-categorical-data, #-categorical-data/-categorical-neural-networks-embedding-layers
