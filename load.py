def load(filepath):
    """
    Loads an image from a specified file path.

    Parameters:
    ----------
    filepath : str
        The file path of the image to load. Can be in formats such as .jpg, .png, .bmp, etc.

    Returns:
    -------
    ndarray
        The loaded image as a NumPy array. The image is converted into a format that can be processed by other functions in the package.

    Raises:
    ------
    FileNotFoundError
        If the specified file does not exist at the given filepath.
    IOError
        If there is an error reading the image file (e.g., corrupted file).

    Examples:
    ---------
    >>> image = load("image.jpg")
    >>> print(type(image))  # <class 'numpy.ndarray'>
    """
    pass
