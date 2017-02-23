#!/usr/bin/env python

__author__ = "Adeel Ahmad"
__email__ = "adeelahmad14@hotmail.com"
__status__ = "Production"

import matplotlib.pyplot as plt
import numpy as np
import skimage as ski
import Image

def cartoonify(im, display=False):
	"""
	 function receives an image and add its gradient magnitude in it and add it
	 to the original image to return a semi-cartoon image.

	 Note: You will have  to scale the gradient-magnitue image
	 before adding it back to the input image.

	 Input:
	    im: input image to cartoonify
	    display: whether to display image or not...

	    NOTE: This function expects a gaussian filtered image
	"""

	kernel, kern_size = np.array([[-1,-1,-1],[0,0,0],[1,1,1]]), 3
	gx, gy = np.zeros_like(im, dtype=float), np.zeros_like(im, dtype=float)

	for i in range(im.shape[0]-(kern_size-1)):
		for j in range(im.shape[1]-(kern_size-1)):
			window = im[i:i+kern_size, j:j+kern_size] 
			gx[i,j], gy[i,j] = np.sum(window * kernel.T), np.sum(window * kernel)																																																																																																																																																																																							

	magnitude = np.sqrt(gx**2 + gy**2)
	magnitude = magnitude.astype(np.int64, copy=False)

	cartoon = im + (im+magnitude)

	if display == 1:
		plt.imshow(cartoon, cmap='gray')
		plt.suptitle('Cartoon')
		plt.show()
	return cartoon
