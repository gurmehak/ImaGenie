import pytest
import numpy as np
from warnings import catch_warnings, simplefilter
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from imagenie.flip import flip

def test_flip():
    """
    Tests the functionality of the flip function based on specific requirements:
    1. Input must be a NumPy array.
    2. Image size must not exceed 1028x1028.
    3. Function should perform the flip correctly.
    4. Invalid directions should default to 0 (horizontal flip).
    """

    # ------------- Mock Data -------------

    # Invalid input (not a NumPy array)
    invalid_input = [[1, 2], [3, 4]]

    # Oversized image (exceeds 1028x1028)
    oversized_image = np.zeros((1030, 1030))

    # Valid input image for functionality tests
    input_image = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    # Expected results for valid inputs
    expected_horizontal = np.array([
        [3, 2, 1],
        [6, 5, 4],
        [9, 8, 7]
    ])
    expected_vertical = np.array([
        [7, 8, 9],
        [4, 5, 6],
        [1, 2, 3]
    ])

    # Invalid directions
    invalid_directions = [2, -1, "invalid", 3.5]


    # ----------------- Tests -----------------

    # Test 1: Input must be a NumPy array
    with pytest.raises(ValueError, match="Input image must be a NumPy array."):
        flip(invalid_input)

    # Test 2: Input image size must not exceed 1028x1028
    with pytest.raises(ValueError, match="Input image size exceeds the 1028x1028 limit."):
        flip(oversized_image)

    # Test 3a: Horizontal flip works correctly
    assert np.array_equal(flip(input_image, direction=0), expected_horizontal), "Horizontal flip failed."

    # Test 3b: Vertical flip works correctly
    assert np.array_equal(flip(input_image, direction=1), expected_vertical), "Vertical flip failed."

    # Test 4a: Invalid directions default to horizontal flip
    for invalid_direction in invalid_directions:
        with catch_warnings(record=True) as warnings_list:
            simplefilter("always")  
            result = flip(input_image, direction=invalid_direction)
            assert len(warnings_list) == 1, f"No warning raised for direction {invalid_direction}."
            assert "Invalid direction" in str(warnings_list[0].message), "Incorrect warning message."
            assert np.array_equal(result, expected_horizontal), f"Invalid direction {invalid_direction} did not default to horizontal flip."

    # Test 4b: `None` as direction defaults to horizontal flip
    result_none = flip(input_image, direction=None)
    assert np.array_equal(result_none, expected_horizontal), "Direction=None did not default to horizontal flip."

