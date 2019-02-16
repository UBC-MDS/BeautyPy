# BeautyPy

<img src="img/logo.png" align="right" height="200" width="200"/>

Image processing tool in Python.

## Contributors

[Gilbert Lei](https://github.com/gilbertlei)

[Jielin Yu](https://github.com/jielinyu)

[Olivia Lin](https://github.com/olivia-lin)

## Overview
Nearly everyone has some experience with Image processing, which is around our daily life. For example, when we use iPhone's camera to take pictures, it allows us to choose a filter which can add some special effects on these pictures. While using these filters, people might have wondered how these special effects are realized.

We developed this package that performs digital image processing on .PNG images. People can use it to transform images into new images with some special effects, such as embossing, to compress images to reduce file sizes, and to calculate the exact number of bytes an image has. We hope to advance and add more functions later on.  

## Functions

#### Emboss

This function turns a colorful image into an embossment-type image. It replace each pixel of the image by either a highlight or a shadow. Low contrast areas are replaced by a gray background.

This function embosses the original image and saves the embossed image to output_path.

*Parameters:*  
- input_path: `string` The file path for the original image we want to emboss.  
- output_path: `string` The file path to save the embossed image.

*Return:*   
- An image file will be saved in output path.


#### Flip

This function flips the images either vertically or horizontally and save it to the output path.

*Parameters:*  
- input_path: `string` The file path for the original image we want to flip.
- output_path: `string`  The file path to save the flipped image.
- direction: `string` Direction to flip, "h" or "v", which represents horizontal and vertical respectively.

*Return:*  
- An embossed image file will be saved in output path.


#### Get_Image_Details

This function returns attributes of the input image, such as dimension, width, height and aspect ratio. Users can choose the attributes they want to look at by specify the name of attribute.

*Parameters:*  
- nput_path: `string` The file path for the image we want to return information of.
- detail: `string` The name of attribute that the function will return. Default set to be 'All'. Available choices are: 'All', 'Dimension', 'Width', 'Height', and 'Aspect Ratio'.

*Return:*  
- A data frame that has the detailed information about input image.


## Similar packages in Python  
For image embossing, there are many tools out there. For example, [PineTools](https://pinetools.com/emboss-effect-image) provide an online tool with which people can emboss images instantly. However, the emboss tool from PineTools is not perfect. Theoretically, an emboss image should be grayscale. However, an embossed image from PineTools has some color on some edges. We decided to develop a new emboss tool that has no such problems. At the same time, we wanted to gain deeper understanding of neural network by coding an emboss algorithm.   


In python, package `scikit-image` can process images.[flip](https://scikit-image.org/)


Function `bytearray` works as the same as our function `Calculate_Bytes`
[bytearray](https://www.programiz.com/python-programming/methods/built-in/bytearray)

Our package focus on emboss, rotate function. This package rewrites some functions in the existing package. It uses matrix computation to process images.
