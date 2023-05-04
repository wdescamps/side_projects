**Model Type:**  Image Generation Models
**Data Type:**  Image Data

## Use Cases :

a. Image colorization: Transforming black and white images into colored versions by learning color patterns from colored examples.

b. Style transfer: Applying an artistic style (e.g., Van Gogh's Starry Night) to another image, creating an artistic rendition of the image.

c. Satellite-to-map translation: Converting satellite images into map-like structures, allowing for automated map generation.


## Python code: 
Here's an example using TensorFlow, building upon the TensorFlow Pix2Pix tutorial:

```python
import tensorflow as tf
import os
import time
from matplotlib import pyplot as plt
from IPython import display

_URL = 'https://people.eecs.berkeley.edu/~tinghuiz/projects/pix2pix/datasets/facades.tar.gz'
path_to_zip = tf.keras.utils.get_file('facades.tar.gz', origin=_URL, extract=True)
PATH = os.path.join(os.path.dirname(path_to_zip), 'facades/')

# Load the dataset
BUFFER_SIZE = 400
BATCH_SIZE = 1
IMG_WIDTH = 256
IMG_HEIGHT = 256

def load(image_file):
    image = tf.io.read_file(image_file)
    image = tf.image.decode_jpeg(image)

    w = tf.shape(image)[1]

    w = w // 2
    real_image = image[:, :w, :]
    input_image = image[:, w:, :]

    input_image = tf.cast(input_image, tf.float32)
    real_image = tf.cast(real_image, tf.float32)

    return input_image, real_image

def resize(input_image, real_image, height, width):
    input_image = tf.image.resize(input_image, [height, width], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    real_image = tf.image.resize(real_image, [height, width], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)

    return input_image, real_image

def random_crop(input_image, real_image):
    stacked_image = tf.stack([input_image, real_image], axis=0)
    cropped_image = tf.image.random_crop(stacked_image, size=[2, IMG_HEIGHT, IMG_WIDTH, 3])

    return cropped_image[0], cropped_image[1]

def normalize(input_image, real_image):
    input_image = (input_image / 127.5) - 1
    real_image = (real_image / 127.5) - 1

    return input_image, real_image

def preprocess_data(input_image, real_image):
    input_image, real_image = resize(input_image, real_image, 286, 286)
    input_image, real_image = random_crop(input_image, real_image)
    input_image, real_image = normalize(input_image, real_image)
    return input_image, real_image

def load_image_train(image_file):
    input_image, real_image = load(image_file)
    input_image, real_image = preprocess_data(input_image, real_image)
    return input_image, real_image

def load_image_test(image_file):
    input_image, real_image = load(image_file)
    input_image, real_image = resize(input_image, real_image, IMG_HEIGHT, IMG_WIDTH)
    input_image, real_image = normalize(input_image, real_image)
    return input_image, real_image

train_dataset = tf.data.Dataset.list_files(PATH + 'train/*.jpg')
train_dataset = train_dataset.map(load_image_train,  num_parallel_calls=tf.data.AUTOTUNE)
train_dataset = train_dataset.shuffle(BUFFER_SIZE)
train_dataset = train_dataset.batch(BATCH_SIZE)
test_dataset = tf.data.Dataset.list_files(PATH + 'test/*.jpg')
test_dataset = test_dataset.map(load_image_test)
test_dataset = test_dataset.batch(BATCH_SIZE)

# Model setup and training
OUTPUT_CHANNELS = 3
EPOCHS = 150

from tensorflow_examples.models.pix2pix import pix2pix

generator = pix2pix.unet_generator(OUTPUT_CHANNELS, norm_type='instancenorm')
discriminator = pix2pix.discriminator(norm_type='instancenorm', target=False)

optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)

def generator_loss(disc_generated_output, gen_output, target):
    gan_loss = tf.keras.losses.BinaryCrossentropy(from_logits=True)(tf.ones_like(disc_generated_output), disc_generated_output)
    l1_loss = tf.reduce_mean(tf.abs(target - gen_output))
    total_gen_loss = gan_loss + (100 * l1_loss)
    return total_gen_loss

def discriminator_loss(disc_real_output, disc_generated_output):
    real_loss = tf.keras.losses.BinaryCrossentropy(from_logits=True)(tf.ones_like(disc_real_output), disc_real_output)
    generated_loss = tf.keras.losses.BinaryCrossentropy(from_logits=True)(tf.zeros_like(disc_generated_output), disc_generated_output)
    total_disc_loss = real_loss + generated_loss
    return total_disc_loss

def train_step(input_image, target, epoch):
    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        gen_output = generator(input_image, training=True)

        disc_real_output = discriminator([input_image, target], training=True)
        disc_generated_output = discriminator([input_image, gen_output], training=True)

        gen_loss = generator_loss(disc_generated_output, gen_output, target)
        disc_loss = discriminator_loss(disc_real_output, disc_generated_output)

    generator_gradients = gen_tape.gradient(gen_loss, generator.trainable_variables)
    discriminator_gradients = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

    optimizer.apply_gradients(zip(generator_gradients, generator.trainable_variables))
    optimizer.apply_gradients(zip(discriminator_gradients, discriminator.trainable_variables))

def fit(train_ds, epochs, test_ds):
    for epoch in range(epochs):
        start = time.time()
        display.clear_output(wait=True)
        for input_image, target in test_ds.take(1):
            generate_images(generator, input_image, target)
        for in_image, tgt in train_ds:
            train_step(in_image, tgt, epoch)
        print(f'Time taken for epoch {epoch + 1} is {time.time() - start} sec.')

# Generate Images
def generate_images(model, test_input, tar):
    prediction = model(test_input, training=True)
    plt.figure(figsize=(15, 15))

    display_list = [test_input[0], tar[0], prediction[0]]
    title = ['Input Image', 'Ground Truth', 'Predicted Image']
    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.title(title[i])
        plt.imshow(display_list[i] * 0.5 + 0.5)
        plt.axis('off')
    plt.show()

fit(train_dataset, EPOCHS, test_dataset)
```


## Resources

a. Original Pix2Pix research paper: https://arxiv.org/abs/1611.07004
b. Tensorflow Pix2Pix tutorial: https://www.tensorflow.org/tutorials/generative/pix2pix
c. PyTorch implementation of Pix2Pix: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

**See Also**:

- [[ Convolutional Neural Networks (CNN)]]
- [[ ResNet]]
- [[ Inception]]
- [[ VGG]]
- [[ MobileNet]]
- [[ DenseNet]]
- [[ EfficientNet]]
- [[ Variational Autoencoders (VAE)]]
- [[ Generative Adversarial Networks (GAN)]]
- [[ StyleGAN]]
- [[ CycleGAN]]

---
tags: #imagedata, #imagedata/pix2pix
