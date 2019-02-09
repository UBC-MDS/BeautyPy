#! /usr/bin/env Rscript

##################################################
## Project: test_emboss.R
## Date: Feb 8th, 2019
## Author: Gilbert Lei, Jielin Yu, Olivia Lin
## Script purpose: This scripts is an unit test for the emboss.R function
##
## Example: Rscript tests/testthat/test_emboss.R
##################################################

import numpy as np
import pytest
import matplotlib.image as mpimg

# initiate file paths
test_input_file_path = "test_imgs/emboss/test_input.jpg"
test_output_file_path = "test_imgs/emboss/test_output.jpg"
# exp_output_file_path = "test_imgs/emboss/exp_output.jpg"

# prepare test input image array
test_input = np.array([[[199, 160, 155], [199, 158, 152], [201, 158, 152], [202, 157, 152], [198, 159, 154]],
                      [[202, 167, 163], [202, 165, 159], [200, 163, 157], [199, 160, 153], [200, 161, 156]],
                      [[205, 174, 169], [202, 171, 166], [200, 167, 160], [198, 165, 158], [198, 159, 154]],
                      [[199, 171, 167], [195, 166, 160], [191, 162, 156], [190, 160, 152], [196, 155, 151]],
                      [[200, 159, 155], [197, 156, 150], [196, 155, 149], [196, 155, 149], [194, 155, 150]],
                      [[197, 156, 150], [196, 155, 149], [196, 155, 149], [196, 155, 149], [194, 155, 150]],
                      [[194, 153, 147], [194, 153, 147], [195, 154, 148], [196, 155, 149], [196, 155, 149]],
                      [[193, 150, 144], [195, 152, 145], [197, 154, 147], [197, 154, 147], [196, 155, 149]],
                      [[193, 150, 143], [195, 152, 145], [197, 154, 147], [198, 155, 148], [196, 155, 149]],
                      [[194, 151, 142], [196, 153, 144], [197, 154, 145], [198, 155, 146], [195, 155, 147]],
                      [[195, 151, 142], [197, 153, 144], [198, 155, 146], [198, 155, 146], [197, 154, 147]]],
                     dtype="uint8")

# save test input image array as a file on computer
mpimg.imsave(test_input_file_path, test_input)

# prepare expected output image array
exp_output = np.array([[[18,18,18], [12,12,12], [1, 1, 1]],
                       [[12,12,12], [9, 9, 9], [1, 1, 1]],
                       [[4, 4, 4], [4, 4, 4], [1, 1, 1]],
                       [[2, 2, 2], [2, 2, 2], [1, 1, 1]],
                       [[0, 0, 0], [255, 255, 255], [1, 1, 1]],
                       [[250, 250, 250], [249, 249, 249], [1, 1, 1]],
                       [[248, 248, 248], [248, 248, 248], [1, 1, 1]],
                       [[250, 250, 250], [251, 251, 251], [1, 1, 1]],
                       [[1, 1, 1], [1, 1, 1], [1, 1, 1]]],
                      dtype="uint8")

def test_wrong_file_type():
    with pytest.raises(TypeError):
        emboss("test_imgs/emboss/input.pdf", test_output_file_path)

def test_non_string_input():
    with pytest.raises(AttributeError):
        emboss(989999999999, test_output_file_path)

def test_non_string_output():
    with pytest.raises(AttributeError):
        emboss(test_input_file_path, 2384957372628)

def test_nonexistent_input_path():
    with pytest.raises(FileNotFoundError):
        emboss("test_imgs/hello/world.jpg", test_output_file_path)

def test_nonexistent_output_path():
    with pytest.raises(FileNotFoundError):
        emboss(test_input_file_path, "test_imgs/hello/world.jpg")

def test_emboss():
    emboss(test_input_file_path, test_output_file_path)
    test_output = mpimg.imread(test_output_file_path)
    assert np.array_equal(test_output, exp_output), "The emboss function does not work properly."
