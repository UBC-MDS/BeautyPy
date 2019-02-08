#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.image as mpimg

def compress(input_path, output_path):
    input_img = mpimg.imread(input_path)

    mpimg.imsave(output_path, output_img)

    return
