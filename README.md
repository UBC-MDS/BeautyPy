# BeautyPy

<img src="img/logo.png" align="right" height="200" width="200"/>

Image processing tool in Python.

## Contributors

[Gilbert Lei](https://github.com/gilbertlei)

[Jielin Yu](https://github.com/jielinyu)

[Olivia Lin](https://github.com/olivia-lin)

## Overview
Nearly everyone has some experience with Image processing, which is around our daily life. For example, when we use iPhone's camera to take pictures, it allows us to choose a filter which can add some special effects on these pictures. While using these filters, people might have wondered how these special effects are realized.

We developed this package that performs digital image processing on .jpg images. People can use it to transform images into new images with some special effects, such as embossing, compress images to reduce file sizes, and calculate the exact number of bytes an image has. We hope to advance and add more functions later on.  

## Functions
**Emboss**  
This function turns a colorful image into an embossment-type image. It replace each pixel of the image by either a highlight or a shadow. Low contrast areas are replaced by a gray background.

**Compress**  
This function compresses an image by 50% on both height and width dimensions. It uses seam-carving method to remove low energy pixels and reduce the size of the original image. Output image may look a little bit different from the original image.  

**Calculate_Bytes**  
This function calculates the bytes size of an image.

## Similar packages in Python

In python, package `OpenCv` can process images.
Specifically, function `cv2.blur` works as the same as our function `blur`, which can blur the image. It is achieved by convolving the image with an average filter. [cv2.blur](https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html)

Function `cv2.cvtColor` works as the same as our function `emboss`, which can change image's color to gray. Additionally, parameter  ?cv2.COLOR_BGR2GRAY? can change image's color to gray. [cv2.cvtColor](https://extr3metech.wordpress.com/2012/09/23/convert-photo-to-grayscale-with-python-opencv/)

Function `cv2.Canny` works as the same as our function `sketch`, which can detect image's edge.
[cv2.Canny](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html)
