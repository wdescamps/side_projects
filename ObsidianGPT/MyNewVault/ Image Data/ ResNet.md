#  ResNet
**Model Type:**  Computer Vision Models
**Data Type:**  Image Data

**Python code **:


In this example, we will use PyTorch and a pre-trained ResNet model to classify an image:

```python
import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision.models import resnet50


def load_image(img_path, transform=None):
    img = Image.open(img_path).convert("RGB")
    if transform:
        img = transform(img)
    img.unsqueeze_(0)
    return img


def predict(model, img_tensor):
    outputs = model(img_tensor)
    _, preds = torch.max(outputs, 1)
    return preds.item()


if __name__ == "__main__":
    # Load a pre-trained ResNet50 model
    model = resnet50(pretrained=True)
    model.eval()

    # Define input image transformation
    transform = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
            ),
        ]
    )

    # Load and transform the input image
    img_path = "path/to/your/image.jpg"
    img_tensor = load_image(img_path, transform=transform)

    # Make a prediction
    prediction = predict(model, img_tensor)
    print(f"Predicted class: {prediction}")
```

Replace "path/to/your/image.jpg" with the path to an image on your local machine to test the model.


**See Also**:

- [[ Convolutional Neural Networks (CNN)]]
- [[ Inception]]
- [[ VGG]]
- [[ MobileNet]]
- [[ DenseNet]]
- [[ EfficientNet]]
- [[ Variational Autoencoders (VAE)]]
- [[ Generative Adversarial Networks (GAN)]]
- [[ StyleGAN]]
- [[ Pix2Pix]]
- [[ CycleGAN]]
## Resources

a) Deep Residual Networks paper: Official research paper introducing ResNet by the authors (Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun).
Link: https://arxiv.org/abs/1512.03385
b) TensorFlow documentation on ResNet: Official TensorFlow tutorial on building and training a ResNet model for image classification.
Link: https://www.tensorflow.org/tutorials/images/deep_cnn_resnet
c) PyTorch Image Models (timm): A collection of image models, layers, utilities, optimizers, and schedulers for PyTorch, which includes pretrained ResNet models.
Link: https://github.com/rwightman/pytorch-image-models


---
tags: #-image-data, #-image-data/-resnet
