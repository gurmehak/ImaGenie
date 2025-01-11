def augment(images, operations):
    """
    Applies a sequence of augmentation operations to a list of images.

    Parameters:
    ----------
    images : list of ndarray
        A list of images (as NumPy arrays) to process.
    operations : list of tuple
        A list of operations to apply, where each operation is a tuple
        (function, *args, **kwargs).
        Example: [(flip, 1), (scale, 0.5), (blur, 5)]

    Returns:
    -------
    list of ndarray
        The list of augmented images.
    """
    
    pass