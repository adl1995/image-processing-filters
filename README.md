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

$$
\Gamma(z) = 
 \frac{1}{W_p} \sum_{x_i \in \Omega} I(x_i)f_r(\|I(x_i)-I(x)\|)g_s(\|x_i-x\|),
,.
$$

Function description: 

bFilter(I, sigmad, sigmar, display)
>  I: input image of type uint8
       > sigmad = sigma for the spatial spread
       > sigmar = sigma for the pixel values (intensities) spread .
       > display = True or False

#### <i class=""></i> Gaussian Filter

 Creates a blurring effect in an image. It is a widely used effect in graphics software, typically to reduce image noise and reduce detail

$$
\Gamma(z) = 
 G(x,y)={\frac {1}{2\pi \sigma ^{2}}}e^{-{\frac {x^{2}+y^{2}}{2\sigma ^{2}}}}
$$

Function description: 

gFilter(sigma):
>  sigma: for blurring intensity


#### <i class=""></i> Cartoonification

Receives an image and adds its gradient magnitude in it and returns a semi-cartoon image after adding the result in the original image. 

Function description: 

cartoonify(im, display=False):
>  im: image to cartoonify
>  display: whether to display the image or not