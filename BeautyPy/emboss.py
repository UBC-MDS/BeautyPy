#!/usr/bin/env python
# coding: utf-8

##################################################
## Project: emboss.py
## Date: Feb 12th, 2019
## Author: Gilbert Lei, Jielin Yu, Olivia Lin
## Purpose: implement the emboss function 
##################################################

import numpy as np
import matplotlib.image as mpimg

def emboss(input_path, output_path):

    '''
    This function embosses the original image and saves the embossed image to output_path.

    Parameters
    ---------------------------------------
    input_path -> the file path for the original image we want to emboss
    output_path ->  the file path to save the embossed image

    Return
    ---------------------------------------
    NA
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

                neighbors = [[tl, tm, tr],
                             [ml, mm, mr],
                             [tr, mr, br]]

                # transform each pixel's r/g/b value using `emboss_filter` 
                rgb.append(np.sum(np.dot(neighbors, emboss_filter)) + 128)
            
            # based on transformed r/g/b values, use below grayscale equation to get new color for each pixel 
            newcolor = 0.3*rgb[0] + 0.59*rgb[1] + 0.11*rgb[2]
            
            # store new color into output array 
            output_img[i-1][j-1][0] = min(255, max(0, newcolor))
            output_img[i-1][j-1][1] = min(255, max(0, newcolor))
            output_img[i-1][j-1][2] = min(255, max(0, newcolor))

    try: 
        # save output array as an image file
        mpimg.imsave(output_path, output_img) 
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
