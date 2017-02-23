#!/usr/bin/env python

__author__ = "Adeel Ahmad"
__email__ = "adeelahmad14@hotmail.com"
__status__ = "Production"

def gFilter(sigma):
    kernel = np.zeros((4*sigma+1,4*sigma+1))

    x = -2 * sigma
    while(x<2 * sigma + 1):
        y = -2 * sigma
        while(y<2 * sigma + 1):
            norm = 1/((2 * 3.14159)*(sigma**2))
            num = (x**2.0) + (y**2)
            denm = 2.0 * (sigma**2)
            kernel[x+2 * sigma, y+2 * sigma] = norm * exp(-num/denm)
            y+=1
        x+=1

    return kernel
