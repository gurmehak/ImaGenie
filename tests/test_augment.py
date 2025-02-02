import numpy as np
import pytest
import matplotlib.pyplot as plt
from imagenie.augment import augment
from imagenie.flip import flip  
from imagenie.scale import scale  
from imagenie.grayscale import grayscale  
from imagenie.blur import blur 

def test_augment():
    """
    Tests the augment function based on the following requirements.
    1. Input should be a list of NumPy arrays.
    2. The operations should be applied correctly.
    3. An error should be raised if an invalid function is used.
    4. Output should produce a list of numpy arrays.
    
    """
    
    # ------------- Mock Data -------------
    input_image = [np.asarray(plt.imread("tests/testimage.png"))]
    output_image = np.asarray(plt.imread('tests/output.png'))
    output_image = output_image[:,:,0:3]
    invalid_input = ["not_an_array"]
    input_single = np.asarray(plt.imread("tests/testimage.png"))

    # Operations
    operations = [(flip, 1), (scale, 0.5), (blur, 1)]
    
    # Run augment function
    augmented_images = augment(input_image, operations)


    # --------------- Tests ---------------
    

    # Test 1: Input should be a list of NumPy arrays.
    with pytest.raises(ValueError, match="Input image must be a NumPy array."):
        augment(invalid_input, operations)

    assert isinstance(input_image, list), "Input must be a list of images."
    

    # Test 2: Check if operations are applied correctly
    assert np.isclose(blur(input_image[0]),output_image,atol=.01).all, "Incorrect output, function not working as expected"

    assert np.isclose(augment(input_image, operations), blur(scale(flip(input_single,1),0.5),1),atol=.01).all, "Incorrect output, function not working as expected"
    

    # Test 3: Check if invalid functions raise a ValueError
    invalid_operations = [(blur,1),(flip, 1), (scale, 1), (lambda x: x, 1)]  # Invalid function (lambda)
    with pytest.raises(ValueError):
        augment(input_image, invalid_operations)
  
    invalid_operations_2 = [(flip, 1), (scale, 0.5), (blur, 1), (lambda x: x, 1)]
    with pytest.raises(ValueError):
        augment(input_image, invalid_operations_2)


    # Test 4: Check if the result is a list of NumPy arrays
    assert isinstance(augmented_images, list), "Output should be a list of images."
    for image in augmented_images:
        assert isinstance(image, np.ndarray), "Each item in the list should be a NumPy array."


if __name__ == "__main__":
    test_augment()
    print("All tests passed.")