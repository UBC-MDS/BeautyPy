#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.image as mpimg

def calculate_bytes(input_path):

    '''
    This function calculate the size, in bytes, of a given image.

    Parameters
    ---------------------------------------
    input_path -> the file path for the image we want to calculate the byte size of

    Return
    ---------------------------------------
    numeric value of the image size, the unit is bytes
    '''

    input_img = mpimg.imread(input_path)

    return
