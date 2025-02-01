# ImaGenie

ImaGenie is a Python package for image augmentation and modification, providing a variety of functions to manipulate images for machine learning, computer vision, or creative purposes. Whether you need to flip, scale, convert to grayscale, or blur images, ImaGenie is your one-stop solution for fast and efficient image manipulation.

## Features

* `flip(image, direction=0)`: Flips the input image either horizontally or vertically. Useful for augmenting datasets by introducing mirror-image variations.
* `scale(image, N)`: Resizes the input image by a given scale factor `N`. This is crucial for normalizing or creating variations in image resolution.
* `blur(image, stdev=1.0, radius=None)`: Applies a Gaussian blur effect to the image. Helps simulate real-world noise or reduce sharpness for specific use cases.
* `greyscale(image)`: Converts the image to grayscale. Ideal for models that only require intensity information, excluding color features.
* `augment(image)`: Applies a sequence of user-defined augmentation operations to a list of images. Useful for image generating images for computer vision tasks.

## Installation

```bash
$ pip install imagenie
```


## **Usage**
### **Grayscale Function**
The `grayscale(image)` function converts an image to grayscale using a weighted sum approach, preserving intensity information while removing color.

### **1️ Convert an RGB Image to Grayscale**
```python
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from imagenie.grayscale import grayscale

# Load an RGB image as a NumPy array
image_path = "img/capybara.jpeg"
image = np.array(Image.open(image_path))

# Convert to grayscale
gray_image = grayscale(image)

# Display the original and grayscale images side by side
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(image)
ax[0].set_title("Original Image")
ax[0].axis("off")

ax[1].imshow(gray_image, cmap="gray")
ax[1].set_title("Grayscale Image")
ax[1].axis("off")

plt.show()
```
**Expected Output**:  
The left side shows the original image, while the right side displays the grayscale version.

---

### **2️ Handling Already Grayscale Images**
If an image is already grayscale (a 2D array), `grayscale(image)` **returns it unchanged**.
```python
# Example of a grayscale image (2D array)
gray_input = np.array([[100, 150, 200], [50, 125, 175]], dtype=np.uint8)

# Function should return the same array
result = grayscale(gray_input)

print("Is unchanged:", np.array_equal(gray_input, result))  # Output: True
```

---

### **3️ Handling Invalid Inputs**
The function raises errors when given invalid inputs.

#### **Invalid Type (Non-NumPy Array)**
```python
try:
    grayscale([[255, 0, 0], [0, 255, 0]])  # List instead of NumPy array
except TypeError as e:
    print(e)
```
**Expected Output**:  
```
The input image must be a NumPy array.
```

#### **Invalid Dimensions**
```python
try:
    grayscale(np.random.rand(5, 5, 4))  # 4-channel image instead of 3-channel RGB
except ValueError as e:
    print(e)
```
**Expected Output**:  
```
The input image must have 3 channels in the last dimension for RGB.
```

---

### **4️ Batch Processing Multiple Images**
You can convert an entire folder of images to grayscale automatically.
```python
import os

def batch_grayscale(image_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir(image_dir):
        img_path = os.path.join(image_dir, file_name)
        if img_path.endswith(".jpeg"):
            img = np.array(Image.open(img_path))
            gray_img = grayscale(img)
            output_path = os.path.join(output_dir, file_name)
            Image.fromarray(gray_img).save(output_path)

# Apply to a folder of images
batch_grayscale("img", "output")
```
**Expected Output**:  
- Grayscale versions of all images are saved in the `"output/"` directory.


## Python Ecosystem Integration

ImaGenie fits well within the Python ecosystem by providing functionality for image manipulation and augmentation. There are several popular libraries for image processing, that offer more complex functionalities, but this package provides a simple, user-friendly interface for common operations tailored for specific image manipulation tasks. 

Reference for other image processing libraries:
- PIL (Python Imaging Library): [PIL](https://python-pillow.org/)
- OpenCV: [OpenCV](https://opencv.org/)
- Augmentor: [Augmentor](https://github.com/mdbloice/Augmentor)

## Contributors

- Agam Sanghera
- Gurmehak Kaur
- Yuhan Fan
- Yichun Liu

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`imagenie` was created by Agam Sanghera, Gurmehak Kaur, Yuhan Fan, Yichun Liu. It is licensed under the terms of the MIT license.

## Credits

`imagenie` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

