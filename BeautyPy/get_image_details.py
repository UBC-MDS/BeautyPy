#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from PIL import Image
import skimage.io

def get_image_details(test_input_file_path, detail = 'All'):

    '''
    This function returns details about the image, such as dimension, width, height, and image ratio.

    Parameters
    ---------------------------------------
    test_input_file_path (string) ->  The file path for the image we want to return information of.
    detail (string) -> The name of attribute that the function will return. Default set to be 'All'.
                        Available choices are: 'All', 'Dimension', 'Width', 'Height', and 'Aspect Ratio'.

    Return
    ---------------------------------------
    A data frame that has the detailed information about input image.
    '''

    try:
        # read input image
        input_img = skimage.io.imread(test_input_file_path)
    except FileNotFoundError:
        print("The input path/file does not exist, or the file is not a valid image file.")
        raise
    except AttributeError:
        print("Please provide a string as the path for the input image file.")
        raise
    except Exception as e:
        print("General Error:")
        print(e)
        raise


    # read image dimension
    h = len(input_img)
    w = len(input_img[0])
    d = len(input_img[0][0])

    if w <= h:
        x = w
        y = h
    else:
        x  = h
        y = w


    gcd = 1


    if  y % x == 0:
        gcd = x
    else:
        for i in range(int(np.ceil(y/2)), 0, -1):
            if x % i == 0 and y % i == 0:
                gcd = i
                break

    dimension = str(w) + str(' x ') + str(h)

    ratio = str(int(w/gcd))+ str(' : ')+ str(int(h/gcd))

    details = {'Dimension': dimension, 'Width': w, 'Height': h, 'Aspect Ratio': ratio}

    details_df = pd.DataFrame(details, index = ['Image'])



    if detail == 'All':
        return details_df
    else:
        return pd.DataFrame(details_df[detail])
