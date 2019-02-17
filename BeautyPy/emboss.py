#!/usr/bin/env python
# coding: utf-8

import numpy as np
from PIL import Image
import skimage.io

def emboss(input_path, output_path):

    '''
    This function embosses the original JPG image and saves the embossed image to output_path.

    Parameters
    ---------------------------------------
    input_path (string) -> the file path for the original image we want to emboss
    output_path (string) ->  the file path to save the embossed image

    Return
    ---------------------------------------
    No return. Transformed image will be saved into the output_path
    '''

    try:
        # read input image
        input_img = skimage.io.imread(input_path)
    except FileNotFoundError:
        print("The input path/file does not exist.")
        raise
    except OSError:
        print("The file is not a valid image file.")
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

    # initialize emboss filter
    emboss_filter = np.array([[1, 0, 0],
                              [0, 0, 0],
                              [0, 0, -1]])

    # initialize output image array
    output_img = np.ones((h-2, w-2, d), dtype="uint8")

    # transform the original red/green/blue color of each pixel into new grayscale, embossed value
    for i in range(1, h-2):
        for j in range(1, w-2):
            rgb = []
            for k in range (0, 3):
                tl = input_img[i+1][j-1][k]
                ml = input_img[i][j-1][k]
                bl = input_img[i-1][j-1][k]
                tm = input_img[i+1][j][k]
                mm = input_img[i][j][k]
                bm = input_img[i-1][j][k]
                tr = input_img[i+1][j+1][k]
                mr = input_img[i][j+1][k]
                br = input_img[i-1][j+1][k]

                # store neighbours into a matrix
                neighbors = np.array([[tl, tm, tr],
                                      [ml, mm, mr],
                                      [tr, mr, br]])

                # use `emboss_filter` on each pixel's neighbourhood matrix to transform R/G/B value
                sum = 0
                for row in range(3):
                    for col in range(3):
                        sum += emboss_filter[row, 0] * neighbors[0, col]
                        sum += emboss_filter[row, 1] * neighbors[1, col]
                        sum += emboss_filter[row, 2] * neighbors[2, col]

                rgb.append(sum + 128)

            # for each pixel, transform R/G/B to grayscale
            newcolor = 0.3*rgb[0] + 0.59*rgb[1] + 0.11*rgb[2]

            # set new color for each pixel in output_img array
            output_img[i-1][j-1][0] = min(255, max(0, newcolor))
            output_img[i-1][j-1][1] = min(255, max(0, newcolor))
            output_img[i-1][j-1][2] = min(255, max(0, newcolor))

    outputImage = Image.fromarray(output_img)

    try:
        # save output array as an image file
        outputImage.save(output_path)
    except FileNotFoundError:
        print("The output path does not exist.")
        raise
    except ValueError:
        print("Please provide a valid file path or valid file type in the output path.")
        raise
    except TypeError:
        print("Please provide a string as the path for the output image file.")
        raise
    except Exception as e:
        print("General Error:")
        print(e)
        raise
