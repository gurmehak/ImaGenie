import unittest
import numpy as np
from imagenie import grayscale 

def test_grayscale():
    """
    Test all cases for the grayscale function.

    This function tests the following scenarios:

    1. **Grayscale Image (2D or 3D Black-and-White Array):**
       Ensures that an image already in grayscale (2D array) or black-and-white (3D array with identical channel values) 
       is correctly handled and converted to a 2D grayscale array if necessary.

    2. **Empty Array:**
       Validates that an empty image array is handled correctly and returned as-is.

    3. **Invalid Input Type:**
       Verifies that a `TypeError` is raised when the input is not a NumPy array (e.g., a Python list).

    4. **Input Image Size Limits:**
       Ensures that input images exceeding size limits (e.g., larger than 1028x1028) raise a `ValueError`.
    """

    # Test that a grayscale image (2D array) or black-and-white image (3D array) is handled correctly
    gray_image = np.array([[10, 20, 30], [40, 50, 60]], dtype=np.uint8)
    result = grayscale(gray_image)
    np.testing.assert_array_equal(result, gray_image)

    bw_image = np.array([[[50, 50, 50], [100, 100, 100]],
                         [[150, 150, 150], [200, 200, 200]]], dtype=np.uint8)
    expected_bw_result = np.array([[50, 100], [150, 200]], dtype=np.uint8)
    result = grayscale(bw_image)
    np.testing.assert_array_equal(result, expected_bw_result)

    # Test that an empty array is handled correctly
    empty_image = np.array([], dtype=np.uint8).reshape(0, 0)
    result = grayscale(empty_image)
    np.testing.assert_array_equal(result, empty_image)

    # Test that a TypeError is raised if the input is not a NumPy array
    try:
        grayscale([[255, 0, 0], [0, 255, 0]])  # Input is a Python list, not a NumPy array
    except TypeError as e:
        assert str(e) == "The input image must be a NumPy array."

    # Test that input image exceeding size limits raises ValueError
    large_image = np.random.randint(0, 255, (1030, 1030, 3), dtype=np.uint8)
    try:
        grayscale(large_image)
    except ValueError as e:
        assert str(e) == "Input image exceeds size limits of 1028x1028."

if __name__ == "__main__":
    test_grayscale()
    print("All tests passed.")
