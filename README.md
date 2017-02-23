Various image processing tools / filter built using Python
===================


List of implemented filters / algorithms:

- Bilateral filter
- Gaussian filter
- Cartoonification
- Local Histogram plotter

----------


Description and Usage
-------------

#### <i class=""></i> Bilateral Filter

 A non-linear, edge-preserving and noise-reducing smoothing filter for images.

![](https://latex.codecogs.com/gif.latex?\Gamma(z)&space;=&space;\frac{1}{W_p}&space;\sum_{x_i&space;\in&space;\Omega}&space;I(x_i)f_r(\|I(x_i)-I(x)\|)g_s(\|x_i-x\|),)

Function description: 

bFilter(I, sigmad, sigmar, display)
>  I: input image of type uint8
       > sigmad = sigma for the spatial spread
       > sigmar = sigma for the pixel values (intensities) spread .
       > display = True or False

#### <i class=""></i> Gaussian Filter

 Creates a blurring effect in an image. It is a widely used effect in graphics software, typically to reduce image noise and reduce detail

![](https://latex.codecogs.com/svg.latex?\Gamma(z)&space;=&space;G(x,y)={\frac&space;{1}{2\pi&space;\sigma&space;^{2}}}e^{-{\frac&space;{x^{2}&plus;y^{2}}{2\sigma&space;^{2}}}})
 ^{2}}}e^{-{\frac {x^{2}+y^{2}}{2\sigma ^{2}}}}" /></a>

Function description: 

gFilter(sigma):
>  sigma: for blurring intensity


#### <i class=""></i> Cartoonify

Receives an image and adds its gradient magnitude in it and returns a semi-cartoon image after adding the result in the original image. 

Function description: 

cartoonify(im, display=False):
>  im: image to cartoonify
>  display: whether to display the image or not

#### <i class=""></i> Sketch

Generates a sketch of given image

Function description: 

rgb2sketch(img, filter_size):
>  img: image
>  filter_size: size of filter to apply

#### <i class=""></i> Local Histogram Generator

Generates a histogram with variable number of bins computer using the filter size  

Function description: 

localHistEq(img, filter_size):
>  img: image
>  filter_size: determines the number of bins and local area