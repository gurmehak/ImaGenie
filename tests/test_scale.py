from imagenie.scale import scale
import numpy as np
import matplotlib.pyplot as plt
import pytest


def test_scale():
    """Test scale function.
    1. test when the scaling factor is not an integer or float
    2. test when the scaling factor is not positive
    3. test when the input image is not a numpy array
    4. test when the original input image exceeds 1028 * 1028
    5. test when the scaled image exceeds 2018 * 1028
    
    """
    
    file_path = "tests/testimage.png"
    file_path_large = 'tests/testimage_large.jpg'
    
    img_array=plt.imread(file_path)
    img_array_large=plt.imread(file_path_large)
    
    example = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]], dtype = np.uint8)
    output = np.array([[[ 0,  1,  2], [ 1,  2,  3], [ 2,  3,  4], [ 3,  4,  5]],
                       [[ 2,  3,  4], [ 2,  3,  4], [ 4,  5,  6], [ 5,  6,  7]],
                       [[ 5,  6,  7], [ 5,  6,  7], [ 7,  8,  9], [ 8,  9, 10]],
                       [[ 6,  7,  8], [ 7,  8,  9], [ 8,  9, 10], [ 9, 10, 11]]], dtype=np.uint8)
    
    assert np.array_equal(scale(example, 2), output)


    # `scale` should throw an error when incorrect types are passed to the scaling factor argument
    with pytest.raises(TypeError):
        scale(img_array, '33')
        
    with pytest.raises(ValueError):
        scale(img_array, -1)
        
    with pytest.raises(TypeError):
        scale(100,2)
        
    # `scale` should throw a warning when the input or scaled image exceeds 1028 * 1028
    with pytest.warns(UserWarning, match = "The input image exceeds the maximum size of 1028x1028."):
        scale(img_array_large, 1)
        
    with pytest.warns(UserWarning, match = "The scaled image exceeds the maximum size of 1028x1028 and need resizing."):
        scale(img_array, 10)
        
    # Test correct scaling output
    scaled_img = scale(img_array, 0.5)
    assert isinstance(scaled_img, np.ndarray), "The output should be a NumPy array."