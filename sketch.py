#!/usr/bin/env python

__author__ = "Adeel Ahmad"
__email__ = "adeelahmad14@hotmail.com"
__status__ = "Production"

import matplotlib.pyplot as plt
import numpy as np
import skimage as ski
import Image


def rgb2sketch(img, filter_size=3):
	"""
	 function receives an image and a filter size and returns it sketch

	 Input:
	    im: input image to cartoonify
	    filter_size: size of filter to apply

	    NOTE: This function expects a gaussian filtered image
	"""

	gray = img[:,:,0] * 0.2989 + img[:,:,1] * 0.5870 + img[:,:,2] * 0.1140 # rgb to gray conversion
	comp = 255 - gray # taking complement


	kernel = np.zeros((filter_size,filter_size), dtype=np.float32);
	kernel[:,:] = 1/float(filter_size**2)
	smooth_img = np.zeros_like(comp, dtype=float)

	# applying average filter
	for i in range(comp.shape[0]-(filter_size-1)):
	    for j in range(comp.shape[1]-(filter_size-1)):
	        smooth_img[i,j] = np.sum(comp[i:i+filter_size, j:j+filter_size] * kernel)

	sketch = gray + smooth_img

	# affine transformation
	alpha = 0.5
	sketch = (alpha * gray) + ((1-alpha) * smooth_img)
	for i in range(sketch.shape[0]):
		for j in range(sketch.shape[1]):
			if sketch[i][j] >= 120:
				sketch[i][j] = 255

	# plotting images
	fig = plt.figure()
	a=fig.add_subplot(1,2,1)
	imgplot = plt.imshow(sketch, cmap='gray')

	plt.imshow(sketch, cmap='gray')
	plt.show()

	return sketch