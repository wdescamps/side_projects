#  Generative Adversarial Networks (GAN)
**Model Type:**  Image Generation Models
**Data Type:**  Image Data

**Python code **:


```
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Load and preprocess the data
(x_train, _), (_, _) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype(np.float32) / 255

batch_size = 256
dataset = tf.data.Dataset.from_tensor_slices(x_train).shuffle(10000).batch(batch_size)

# Define the Generator
def generator_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(7*7*256, use_bias=False, input_shape=(100,)))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.ReLU())

    model.add(tf.keras.layers.Reshape((7, 7, 256)))
    model.add(tf.keras.layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.ReLU())

    model.add(tf.keras.layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.ReLU())

    model.add(tf.keras.layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='sigmoid'))
    return model

# Define the Discriminator
def discriminator_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[28, 28, 1]))
    model.add(tf.keras.layers.LeakyReLU())
    model.add(tf.keras.layers.Dropout(0.3))

    model.add(tf.keras.layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'))
    model.add(tf.keras.layers.LeakyReLU())
    model.add(tf.keras.layers.Dropout(0.3))

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(1))
    return model

generator = generator_model()
discriminator = discriminator_model()

# Define loss and optimizers
cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)

def discriminator_loss(real_output, fake_output):
    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    total_loss = real_loss + fake_loss
    return total_loss

def generator_loss(fake_output):
    return cross_entropy(tf.ones_like(fake_output), fake_output)

generator_optimizer = tf.keras.optimizers.Adam(1e-4)
discriminator_optimizer = tf.keras.optimizers.Adam(1e-4)

# Training the GAN
epochs = 50
noise_dim = 100

@tf.function
def train_step(images):
    noise = tf.random.normal([batch_size, noise_dim])
    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = generator(noise, training=True)

        real_output = discriminator(images, training=True)
        fake_output = discriminator(generated_images, training=True)

        gen_loss = generator_loss(fake_output)
        disc_loss = discriminator_loss(real_output, fake_output)

    gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
    gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)
    generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))

def train_gan(epochs, dataset):
    for epoch in range(epochs):
        for image_batch in dataset:
            train_step(image_batch)

# Train the GAN
train_gan(epochs, dataset)

# Generate and display a sample image
sample_noise_vector = tf.random.normal([1, noise_dim])
generated_image = generator(sample_noise_vector, training=False)
generated_image = np.squeeze(generated_image)
plt.imshow(generated_image, cmap='gray')
plt.show()
```

This code demonstrates an implementation of a simple GAN using TensorFlow to generate samples of the MNIST digit dataset. The Generator and Discriminator neural networks are defined, and their respective losses and optimizers are established. The `train_gan` function trains the GAN for the given number of epochs, and then a sample generated image is displayed.


**See Also**:

- [[ Convolutional Neural Networks (CNN)]]
- [[ ResNet]]
- [[ Inception]]
- [[ VGG]]
- [[ MobileNet]]
- [[ DenseNet]]
- [[ EfficientNet]]
- [[ Variational Autoencoders (VAE)]]
- [[ StyleGAN]]
- [[ Pix2Pix]]
- [[ CycleGAN]]
## Resources

a. Generative Adversarial Networks in TensorFlow: An official tutorial from TensorFlow that walks you through the process of implementing a GAN using TensorFlow 2.x.
Link: https://www.tensorflow.org/tutorials/generative/dcgan
b. Keras-GAN: A collection of Keras implementations of GANs, including DCGAN, CycleGAN, and more, which can serve as a starting point for implementing your own GANs using Keras library.
Link: https://github.com/eriklindernoren/Keras-GAN
c. GAN Lab: A visual experiment to interactively learn and understand GANs, by generating samples and observing the training process in real-time, developed by Google.
Link: https://poloclub.github.io/ganlab/


---
tags: #-image-data, #-image-data/-generative-adversarial-networks-gan
