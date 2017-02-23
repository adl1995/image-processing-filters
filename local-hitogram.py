#!/usr/bin/env python

__author__ = "Adeel Ahmad"
__email__ = "adeelahmad14@hotmail.com"
__status__ = "Production"

import matplotlib.pyplot as plt
import numpy as np
import skimage as ski
import Image

def localHistEq(img, filter_size):
	"""
	 function receives an image and a filter size. It returns the local histogram

	 Input:
	    im: input image to cartoonify
	    display: whether to display image or not...

	    NOTE: This function expects a gaussian filtered image
	"""

	heq = np.zeros_like(img)
	for i in range(0, img.shape[0], filter_size):
		for j in range(0, img.shape[1], filter_size):
			window = img[i:i+filter_size,j:j+filter_size]
			hist, bins = np.histogram(window.flatten(),256,[0,256])

			cdf = hist.cumsum()
			cdf_normalized = cdf * (hist.max()/ cdf.max())

			cdf_m = np.ma.masked_equal(cdf,0)
			cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
			cdf = np.ma.filled(cdf_m,0).astype('uint8')

			heq[i:i+filter_size,j:j+filter_size] = cdf[window]
	return heq