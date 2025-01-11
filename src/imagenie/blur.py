def blur(image, stdev=1.0,radius=None):
    """
    Add noise to image using a Gaussian filter

    Parameters:
    ----------
    image : ndarray
        The input image to be blurred, represented as a NumPy array 
        or similar format 
    stdev : Float 
        Standard deviation for Gaussian/Normal distribution used to 
        calculate the value of image pixels after filtering
        Default is 1.0 for Standard Normal Distribution
    radius : Float, optional 
        Radius of the Gaussian kernel

    Returns:
    -------
    ndarray
        The blurred image as a NumPy array.

    Raises:
    ------
    ValueError
        If the specified standard deviation is not positive.

    Examples:
    ---------
    >>> print(image)
        [0.10196079, 0.627451  , 0.74509805],
        [0.11372549, 0.6666667 , 0.78431374],
        [0.1254902 , 0.7058824 , 0.81960785]
    >>> blur(image)
        [0.2991612 , 0.5070358 , 0.66973376],
        [0.30862695, 0.52062243, 0.6859944 ],
        [0.31771535, 0.53367144, 0.70153326]
    >>> print(image2)
        [0.09803922, 0.5882353 , 0.70980394],
        [0.1254902 , 0.70980394, 0.8235294 ],
        [0.1254902 , 0.70980394, 0.8235294 ]
    >>> blur(image2,stdev=2)
        [0.49137527, 0.5290323 , 0.56662756],
        [0.49490717, 0.53276986, 0.5705702 ],
        [0.4977027 , 0.5357282 , 0.5736908 ]
    """
    pass