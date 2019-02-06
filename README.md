# BeautyPy
Three filters for image in Python

## Overview
Nearly everyone has some experience with Image processing, which is around our daily life. For example, when we use iPhone's camera to take pictures, it allows us to choose a filter which can add some special effects on these pictures. While using these filters, people might have wondered how these special effects are realized.

We developed this package that performs digital image processing on .jpg images. People can use it to transform images into new images with some special effects. We started this project with three typical image processing effects, including blurring, embossing and sketching, and hope to advance and add more later on.  

## Functions
**Blur**  
This function performs convolution to make a blurred version of the original image so as to de-emphasize the sharpnesses between adjacent pixeles. By averaging every pixel with surroungding pixels, it remove details from the original image.

**Emboss**  
This function turns a colorful image into an embossment-type image. It replace each pixel of the image by either a highlight or a shadow. Low contrast areas are replaced by a gray background.

**Sketch**  
This function detects discontinuities in brightness within an image, finds the boundaries of objects and transform the color image into a gray image with highlighting on these boundaries.
