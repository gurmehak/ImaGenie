from imagenie import imagenie
from imagenie.imagenie import blur
import numpy as np

def test_blur():
    #Test for numpy array
    assert isinstance("A", np.ndarray), "Please make sure input is numpy array"
    assert isinstance(1, np.ndarray), "Please make sure input is numpy array"
    assert isinstance(0.0, np.ndarray), "Please make sure input is numpy array"
    #Test blurring function
    expected = [[0.2991612 , 0.5070358 , 0.66973376],[0.30862695, 0.52062243, 0.6859944 ],[0.31771535, 0.53367144, 0.70153326]]
    actual = blur([[0.10196079, 0.627451  , 0.74509805],[0.11372549, 0.6666667 , 0.78431374],[0.1254902 , 0.7058824 , 0.81960785]])
    assert actual == expected, "Incorrect output, function not working as expected"
    