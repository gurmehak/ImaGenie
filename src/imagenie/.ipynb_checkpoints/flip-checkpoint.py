def flip(image, direction='horizontal'):
    """
    Flips an image either horizontally or vertically.

    Parameters:
    ----------
    image : ndarray
        The input image to be flipped, represented as a NumPy array or similar format.
    direction : str, optional
        The direction in which to flip the image:
        - 0: for horizontal flip (default)
        - 1: vertical flip

    Returns:
    -------
    ndarray
        The flipped image as a NumPy array.

    Raises:
    ------
    ValueError
        If the specified direction is not 1 or 0.

    Examples:
    ---------
    Flip an image horizontally:
    >>> flipped_image = flip_image(image)

    Flip an image vertically:
    >>> flipped_image = flip_image(image, 1)
    """
    pass
