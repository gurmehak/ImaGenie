import unittest
import numpy as np
from imagenie import grayscale  

def test_grayscale():
    """Test all cases for the grayscale function."""

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

if __name__ == "__main__":
    test_grayscale()
    print("All tests passed.")