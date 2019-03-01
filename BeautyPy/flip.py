
# coding: utf-8

# In[ ]:


import numpy as np
import skimage.io
from PIL import Image

def flip(input_path, output_path,direction):

    '''
    This function flips the images either vertically or horizentally and save it to the output path

    Parameters
    ---------------------------------------
    input_path -> the file path for the original image we want to compress
    output_path ->  the file path to save the compressed image
    direction: direction to flip, "h" or "v", which represents horizontal and vertical repectively

    Return
    ---------------------------------------
    an image file saved in output path
    '''
    assert direction in ["h","v"], "Invalid input for direction"

    try:
        # read input image

        input_img = skimage.io.imread(input_path)
    except FileNotFoundError:
        print("The input path/file does not exist, or the file is not a valid image file.")
        raise
    except AttributeError:
        print("Please provide a string as the path for the input image file.")
        raise
    except OSError:
        print("The input file is not an image.")
        raise



    col=input_img.shape[1]
    row=input_img.shape[0]
    output_img=input_img.copy()
    # horizental flip
    if direction == "h":
        for i in range(row):
            for j in range(col):
                output_img[i,j]=input_img[i,col-1-j]
    # vertical flip
    else:
        for i in range(row):
            for j in range(col):
                output_img[i,j]=input_img[row-1-i,j]

    try:
        # save output array as an image file
        img = Image.fromarray(output_img)
        img.save(output_path)

    except FileNotFoundError:
        print("The output path does not exist.")
        raise
    except ValueError:
        print("Please provide a valid file path or valid file type in the output path.")
        raise
