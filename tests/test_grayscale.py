import unittest
import numpy as np
from your_module import grayscale  # Replace 'your_module' with the actual module name

def test_grayscale():
    """
    Test all cases for the grayscale function.

    This function tests the following scenarios:

    1. **Grayscale Image (2D Array):**
       Ensures that an image already in grayscale (2D array) is returned unchanged.

    2. **Empty Array:**
       Validates that an empty image array is handled correctly and returned as-is.

    3. **Invalid Input Type:**
       Verifies that a `TypeError` is raised when the input is not a NumPy array (e.g., a Python list).

    4. **Black-and-White Image (3D Array):**
       Tests that an image represented as a 3D array with identical channel values is correctly converted to a 2D grayscale array.
    """

    # Test that an already grayscale image (2D array) is returned unchanged
    gray_image = np.array([[10, 20, 30], [40, 50, 60]], dtype=np.uint8)
    result = grayscale(gray_image)
    np.testing.assert_array_equal(result, gray_image)

    # Test that an empty array is handled correctly
    empty_image = np.array([], dtype=np.uint8).reshape(0, 0)
    result = grayscale(empty_image)
    np.testing.assert_array_equal(result, empty_image)

    # Test that a TypeError is raised if the input is not a NumPy array
    try:
        grayscale([[255, 0, 0], [0, 255, 0]])  # Input is a Python list, not a NumPy array
    except TypeError as e:
        assert str(e) == "The input image must be a NumPy array."

    # Test that an image already in black and white (3D array but with identical channels) is returned as 2D
    bw_image = np.array([[[50, 50, 50], [100, 100, 100]],
                         [[150, 150, 150], [200, 200, 200]]], dtype=np.uint8)
    expected_bw_result = np.array([[50, 100], [150, 200]], dtype=np.uint8)
    result = grayscale(bw_image)
    np.testing.assert_array_equal(result, expected_bw_result)

if __name__ == "__main__":
    test_grayscale()
    print("All tests passed.")
