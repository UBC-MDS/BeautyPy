#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.image as mpimg

def compress(input_path, output_path):

    '''
    This function compress the original image to about half of its size, and saves the compressed image to path.

    Parameters
    ---------------------------------------
    input_path -> the file path for the original image we want to compress
    output_path ->  the file path to save the compressed image

    Return
    ---------------------------------------
    NA
    '''

    input_img = mpimg.imread(input_path)

    mpimg.imsave(output_path, output_img)

    return
