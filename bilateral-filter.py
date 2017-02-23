#!/usr/bin/env python

__author__ = "Adeel Ahmad"
__email__ = "adeelahmad14@hotmail.com"
__status__ = "Production"

import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from skimage import img_as_float, img_as_ubyte
from skimage import color                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

def bFilter(I, sigmad, sigmar, display):
    """ function applies the bilateral filter on the given image
        Input:
        I: input image of type uint8
        sigmad = sigma for the spatial spread
        sigmar = sigma for the pixel values (intensities) spread .
        display = True or False """

    bilateral = np.zeros_like(I, dtype=float)
    filter_size = sigmad * 3
    center = int(filter_size / 2)  
    for i in range(I.shape[0]-(filter_size-1)):
        for j in range(I.shape[1]-(filter_size-1)):

            sum_pixel = 0.0
            weight = 0.0

            for k in range(i, i+filter_size-1):
                for l in range(j, j+filter_size-1):

                    k, l = float(k), float(l)
                    intensity_kernel = np.exp(-(I[k,l] - I[i+center, j+center])**2 / (2.0 * (sigmar**2)))
                    spatial_kernel = np.exp(-np.sqrt((k - (i+center))**2 + (l-(j+center))**2) / (2.0 * (sigmad**2)))
                    weight += (intensity_kernel * spatial_kernel)
                    sum_pixel += I[k,l] * (intensity_kernel * spatial_kernel)

            bilateral[i,j] = (sum_pixel / weight)


    bilateral = bilateral.astype(np.int64, copy=False)

    if display == 1:
        plt.imshow(bilateral, cmap='gray')
        plt.suptitle('Bilateral')
        plt.show()

    return bilateral

