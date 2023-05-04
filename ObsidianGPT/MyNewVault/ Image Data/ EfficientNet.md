#  EfficientNet
**Model Type:**  Computer Vision Models
**Data Type:**  Image Data

**Python code **:


```python
import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

# Load the pre-trained EfficientNetB0 model without the top layer
base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the base model (use its pre-trained weights)
for layer in base_model.layers:
    layer.trainable = False

# Add a new top layer for a custom classification task
x = base_model.output
x = GlobalAveragePooling2D()(x)
predictions = Dense(5, activation='softmax')(x)

# Create the final model
model = Model(inputs=base_model.input, outputs=predictions)

# Compile the model
model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model with custom dataset
# Replace `train_data`, `train_labels` with your own training data and labels
history = model.fit(train_data, train_labels, epochs=10, batch_size=32, validation_split=0.2)

# Fine-tuning: Unfreeze some layers of the base model and train the model again
for layer in base_model.layers[-20:]:
    layer.trainable = True

model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_data, train_labels, epochs=10, batch_size=32, validation_split=0.2)
```

In this code snippet, we demonstrate how to use the EfficientNetB0 architecture for a custom image classification task. The base model is loaded with pre-trained weights, and the top layer is replaced with a new dense layer for our specific task. After training the model with a custom dataset, we perform fine-tuning by unfreezing some layers of the base model and training again with a lower learning rate.


**See Also**:

- [[ Convolutional Neural Networks (CNN)]]
- [[ ResNet]]
- [[ Inception]]
- [[ VGG]]
- [[ MobileNet]]
- [[ DenseNet]]
- [[ Variational Autoencoders (VAE)]]
- [[ Generative Adversarial Networks (GAN)]]
- [[ StyleGAN]]
- [[ Pix2Pix]]
- [[ CycleGAN]]
## Resources

a. Official EfficientNet GitHub repository: https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet
b. TensorFlow Hub: Offers pre-trained EfficientNet models that can be fine-tuned for various applications: https://tfhub.dev/google/collections/efficientnet/
c. Keras Applications: Provides built-in EfficientNet implementations in the Keras library: https://keras.io/api/applications/#available-models


---
tags: #-image-data, #-image-data/-efficientnet
