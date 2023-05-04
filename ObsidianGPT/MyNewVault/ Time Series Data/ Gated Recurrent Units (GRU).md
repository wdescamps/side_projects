#  Gated Recurrent Units (GRU)
**Model Type:**  Exponential Smoothing State Space Models (ETS)
**Data Type:**  Time Series Data

**Python code **:


```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GRU, Embedding
from tensorflow.keras.utils import to_categorical

# Generate synthetic time series data
def generate_data(num_sequences, sequence_len):
    X = np.random.rand(num_sequences, sequence_len)
    y = X.sum(axis=1) > sequence_len / 2
    return X[..., np.newaxis], to_categorical(y)


# Define GRU model
def build_model(sequence_len):
    model = Sequential()
    model.add(GRU(32, input_shape=(sequence_len, 1)))
    model.add(Dense(2, activation="softmax"))

    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    return model


# Generate and preprocess data
num_sequences = 1000
sequence_len = 20
X, y = generate_data(num_sequences, sequence_len)

# Split the data into training and testing sets
train_X, test_X = X[: int(0.8 * num_sequences)], X[int(0.8 * num_sequences) :]
train_y, test_y = y[: int(0.8 * num_sequences)], y[int(0.8 * num_sequences) :]

# Build and train the GRU model
model = build_model(sequence_len)
model.fit(train_X, train_y, epochs=10, batch_size=32)

# Evaluate the GRU model
loss, accuracy = model.evaluate(test_X, test_y)
print(f"Test accuracy: {accuracy * 100:.2f}%")
```

This code demonstrates how to use a GRU model to classify whether the sum of the elements in a synthetic time series is greater than half the sequence length. The code builds and trains a GRU model using TensorFlow Keras, and prints the test accuracy of the model.


**See Also**:

- [[ Autoregressive Integrated Moving Average (ARIMA)]]
- [[ Seasonal decomposition of time series (STL)]]
- [[ Recurrent Neural Networks (RNN)]]
- [[ Long Short]]
- [[ Facebook Prophet]]
- [[ LightGBM]]
- [[ XGBoost]]
## Resources

a. TensorFlow: GRU Layer: Comprehensive documentation on the GRU layer provided by TensorFlow, including detailed information on functionality, parameters, and examples.
Link: https://www.tensorflow.org/api_docs/python/tf/keras/layers/GRU
b. Keras: Sequence classification with GRU: A step-by-step tutorial on how to use Keras to implement a GRU model for sequence classification.
Link: https://keras.io/examples/nlp/pretrained_word_embeddings/
c. Understanding GRUs: A blog post by Chris Olah that visually and intuitively explains the concept and mechanisms of GRUs.
Link: https://colah.github.io/posts/2015-08-Understanding-LSTMs/


---
tags: #-time-series-data, #-time-series-data/-gated-recurrent-units-gru
