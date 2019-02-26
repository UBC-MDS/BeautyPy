# BeautyPy

<img src="img/logo.png" align="right" height="200" width="200"/>

Image processing tool in Python.

## Contributors

[Gilbert Lei](https://github.com/gilbertlei)

[Jielin Yu](https://github.com/jielinyu)

[Olivia Lin](https://github.com/olivia-lin)

## Overview
Nearly everyone has some experience with Image processing, which is around our daily life. For example, when we use iPhone's camera to take pictures, it allows us to choose a filter which can add some special effects on these pictures. While using these filters, people might have wondered how these special effects are realized.

We developed this package that performs digital image processing on .JPG images. People can use it to transform images into new images with some special effects, such as embossing, to compress images to reduce file sizes, and to calculate the exact number of bytes an image has. We hope to advance and add more functions later on.  

## Functions

#### Emboss

This function turns a colorful image into an embossment-type image. It replace each pixel of the image by either a highlight or a shadow. Low contrast areas are replaced by a gray background.

This function embosses the original image and saves the embossed image to output_path.

*Parameters:*  
- input_path: `string` The file path for the original image we want to emboss.  
- output_path: `string` The file path to save the embossed image.

*Return:*   
- An embossed image will be saved in output path.


#### Flip

This function flips the images either vertically or horizontally and save it to the output path.

*Parameters:*  
- input_path: `string` The file path for the original image we want to flip.
- output_path: `string`  The file path to save the flipped image.
- direction: `string` Direction to flip, "h" or "v", which represents horizontal and vertical respectively.

*Return:*  
- An flipped image file will be saved in output path.


#### Get_Image_Details

This function returns attributes of the input image, such as dimension, width, height and aspect ratio. Users can choose the attributes they want to look at by specify the name of attribute.

*Parameters:*  
- input_path: `string` The file path for the image we want to return information of.
- detail: `string` The name of attribute that the function will return. Default set to be 'All'. Available choices are: 'All', 'Dimension', 'Width', 'Height', and 'Aspect Ratio'.

*Return:*  
- A data frame that has the detailed information about input image.




## Installation

```
pip install git+https://github.com/UBC-MDS/BeautyPy
```

## Run Tests

From root directory, run all test files in terminal using below command line:

```
pytest tests/
```

To test a specific function, run any of below commands:
```
pytest tests/test_emboss.py  
pytest tests/test_flip.py  
pytest tests/test_get_image_details.py  
```

## Usage

#### Emboss an image
```
>> from BeautyPy.emboss import emboss
>> emboss("img/Google-logo.jpg", "img/Google-logo_emboss.jpg")
```

#### Flip an image  
```
>> from BeautyPy.flip import flip
>> flip("img/Google-logo.jpg", "img/Google-logo_flip.jpg", "h")  
```

#### Get details of an image  
```
>> from BeautyPy.get_image_details import get_image_details
>> get_image_details("img/Google-logo.jpg")

      Dimension	  Width	  Height	   Aspect Ratio
Image	780 x 439	  780	    439	      780 : 439
```

## Where does this package fit into the Python ecosystem  
For image embossing, there are many tools out there in the Python ecosystem. For example, Python package [PIL](https://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html) provides an emboss filter, along with other filters, with which people can emboss images. However, the `emboss` tool from PIL is not perfect. Theoretically, an emboss image should be grayscale. But an embossed image created from PIL's emboss filter has some colors along some edges. We decided to develop a new emboss tool that has no such problems. At the same time, we wanted to gain deeper understanding of neural network by coding an emboss filter algorithm.   


For image flipping, there are also many packages available in the Python ecosystem. One example is the [flip function](https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#flip) from [OpenCV package](https://pypi.org/project/opencv-python/). However, OpenCV's `flip` function works on an array, instead of an image file saved on a computer. So we decided to develop a `flip` tool that can read in a real image file and save the flipped image as another real file on computer.


For getting image details, a Python function [bytearray](https://www.programiz.com/python-programming/methods/built-in/bytearray)
 works as the same as our function `get_image_details`.
