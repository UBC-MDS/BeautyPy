#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from fractions import gcd
import matplotlib.image as mpimg

def image_details(input_path, detail = 'All'):

    '''
    This function returns details about the image, such as dimension, width, height, and image ratio.

    Parameters
    ---------------------------------------
    input_path (string) ->  The file path for the image we want to return information of.
    detail (string) -> The name of attribute that the function will return. Default set to be 'All'.
                        Available choices are: 'All', 'Dimension', 'Width', 'Height', and 'Aspect Ratio'.

    Return
    ---------------------------------------
    A data frame that has the detailed information about input image.
    '''

    try:
        # read input image
        input_img = mpimg.imread(input_path)
    except FileNotFoundError:
        print("The input path/file does not exist, or the file is not a valid image file.")
        raise
    except TypeError:
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

    if  x % y == 0:
        gcd = y
    else:
        for i in range(ceil(y/2), 0, -1):
            if x % i == 0 and y % i == 0:
                gcd = i
                break

    dimension = str(w) + str(' x ') + str(h)

    ratio = str(int(w/gcd))+ str(' : ')+ str(int(h/gcd))

    details = {'Dimension': dimension, 'Width': w, 'Height': h, 'Aspect Ratio': ratio}

    details_df = pd.DataFrame(details, index = ['Image'])


    try:
        detail == 'All' or detail == 'Dimension' or detail == 'Width' or detail == 'Height' or detail == 'Aspect Ratio'
    except TypeError:
        print("Please provide a string to specify the name of attribute.")
        raise
    except ValueError:
        print("Please provide a valid attribution name,  or simply leave it as default to get complete information.")
        raise
    except Exception as e:
        print("General Error:")
        print(e)
        raise


    if detail == 'All':
        return details_df
    else:
        return pd.DataFrame(details_df[detail])
