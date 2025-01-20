import numpy as np
import pytest
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
    
    """
    
    # ------------- Mock Data -------------
    input_images = [
        np.array([[1, 2], [3, 4]]),
        np.array([[5, 6], [7, 8]])
    ]
    
    # Operations
    operations = [(flip, 1), (scale, 0.5), (blur, 3)]
    
    # Run augment function
    augmented_images = augment(input_images, operations)


    # --------------- Tests ---------------
    
    # Check if the result is a list of NumPy arrays
    assert isinstance(augmented_images, list), "Output should be a list of images."
    for image in augmented_images:
        assert isinstance(image, np.ndarray), "Each item in the list should be a NumPy array."
    
    # Test 2: Check if operations are applied correctly
    # call individual tests 
    
    # Check if invalid functions raise a ValueError
    invalid_operations = [(flip, 1), (scale, 0.5), (grayscale, 0.7), (lambda x: x, 1)]  # Invalid function (lambda)
    with pytest.raises(ValueError, match="Function <lambda> is not allowed"):
        augment(input_images, invalid_operations)
    
    invalid_operations_2 = [(flip, 1), (scale, 0.5), (blur, 3), (lambda x: x, 1)]
    with pytest.raises(ValueError):
        augment(input_images, invalid_operations_2)
