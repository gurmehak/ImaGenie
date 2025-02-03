from imagenie.blur import blur
import numpy as np
import pytest
import matplotlib.pyplot as plt
def test_blur():
    #Test for numpy array
    file_path = "tests/testimage.png"
    file_path_large = 'tests/testimage_large.jpg'
    blurred_path='tests/output.png'
    large_img=np.asarray(plt.imread(file_path_large))
    img_array=np.asarray(plt.imread(file_path))
    expected = np.asarray(plt.imread(blurred_path))
    input= img_array
    with pytest.raises(TypeError):
        blur(input, '33')

    with pytest.raises(ValueError):
        blur(input, -1)
    #Test for non np.ndarray
    with pytest.raises(TypeError):
        blur(100,2)
    with pytest.raises(ValueError, match = "The input image exceeds the maximum size of 1028x1028."):
        blur(large_img)

    
    #Test blurring function
    assert np.isclose(blur(input),expected[:,:,0:3],atol=.01).all, "Incorrect output, function not working as expected"