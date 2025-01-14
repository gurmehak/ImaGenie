import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import rescale


def scale(image, N):
    """Scale an image file by a factor of N.

    Parameters
    ----------
    image : np.array
        The input image to be flipped, represented as a NumPy array or similar format.
    
    N: float
        An non-negative float specifying the scaling factor.

    Returns
    -------
    np.array
        The flipped image as a NumPy array.

    Examples
    --------
    Scale the image 2 times larger. 
    >>> img = scale("testimage.jpg", 2)
    """
    scaled_array = rescale(img, scale=N, channel_axis=-1, anti_aliasing=True)
    
    return scaled_array