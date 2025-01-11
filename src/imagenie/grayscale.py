import numpy as np

def grayscale(image):
    """
    Converts an image to grayscale.

    Parameters:
    ----------
    image : ndarray
        The input image, represented as a NumPy array. It can be a 3D array (RGB) or a 2D array (already grayscale).

    Returns:
    -------
    ndarray
        The grayscale image as a 2D NumPy array.

    Raises:
    ------
    ValueError
        If the input is not a 2D or 3D NumPy array.

    Examples:
    ---------
    Convert an RGB image to grayscale:
    >>> gray_image = grayscale(image)
    """
    # Ensure the input is a valid NumPy array
    if not isinstance(image, np.ndarray):
        raise ValueError("The input image must be a NumPy array.")
    
    # Handle already grayscale (2D) images
    if image.ndim == 2:
        return image
    
    # Handle RGB images (3D)
    elif image.ndim == 3:
        # Use weighted average to convert to grayscale
        # Common weights: 0.2989 for R, 0.5870 for G, 0.1140 for B
        return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    
    else:
        raise ValueError("The input image must be a 2D or 3D NumPy array.")
