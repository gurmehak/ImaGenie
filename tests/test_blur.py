from imagenie import blur
import numpy as np
import pytest
import matplotlib.pyplot as plt
def test_blur():
    #Test for numpy array
    file_path = "tests/testimage.png"
    file_path_large = 'tests/testimage_large.jpg'

    img_array=np.asarray(plt.imread(file_path))
    img_array_large=np.asarray(plt.imread(file_path_large))
    expected = np.array([0.2991612 , 0.5070358 , 0.66973376],[0.30862695, 0.52062243, 0.6859944 ],[0.31771535, 0.53367144, 0.70153326])
    input= np.array([0.10196079, 0.627451  , 0.74509805],[0.11372549, 0.6666667 , 0.78431374],[0.1254902 , 0.7058824 , 0.81960785])
    with pytest.raises(TypeError):
        blur(img_array, '33')

    with pytest.raises(ValueError):
        blur(img_array, -1)

    with pytest.raises(TypeError):
        blur(100,2)

    with pytest.warns(UserWarning, match = "The input image exceeds the maximum size of 1028x1028."):
        blur(img_array_large, 1)

    with pytest.warns(UserWarning, match = "The scaled image exceeds the maximum size of 1028x1028 and need resizing."):
        blur(img_array, 10)

    #Test blurring function
    
    assert blur(input) == expected, "Incorrect output, function not working as expected"
    