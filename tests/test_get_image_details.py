#! /usr/bin/env python

import numpy as np
import pandas as pd
import skimage.io
import pytest
from PIL import Image
from BeautyPy.get_image_details import get_image_details


# prepare test input 1
test_input_1 = np.array([[[199, 160, 155], [199, 158, 152], [201, 158, 152], [202, 157, 152], [198, 159, 154]],
                  [[202, 167, 163], [202, 165, 159], [200, 163, 157], [199, 160, 153], [200, 161, 156]],
                  [[205, 174, 169], [202, 171, 166], [200, 167, 160], [198, 165, 158], [198, 159, 154]],
                  [[199, 171, 167], [195, 166, 160], [191, 162, 156], [190, 160, 152], [196, 155, 151]],
                  [[200, 159, 155], [197, 156, 150], [196, 155, 149], [196, 155, 149], [194, 155, 150]],
                  [[197, 156, 150], [196, 155, 149], [196, 155, 149], [196, 155, 149], [194, 155, 150]],
                  [[194, 153, 147], [194, 153, 147], [195, 154, 148], [196, 155, 149], [196, 155, 149]],
                  [[193, 150, 144], [195, 152, 145], [197, 154, 147], [197, 154, 147], [196, 155, 149]],
                  [[193, 150, 143], [195, 152, 145], [197, 154, 147], [198, 155, 148], [196, 155, 149]],
                  [[194, 151, 142], [196, 153, 144], [197, 154, 145], [198, 155, 146], [195, 155, 147]]],
                 dtype="uint8")

inputImage = Image.fromarray(test_input_1)
inputImage.save("test_imgs/get_image_details/test_input_1.png")

test_input_path_1 = "test_imgs/get_image_details/test_input_1.png"

expexted_detail_1 = {'Dimension': "5 x 10", 'Width': 5, 'Height': 10, 'Aspect Ratio': "1 : 2"}

expected_details_df_1 = pd.DataFrame(expexted_detail_1, index = ['Image'])



# prepare test input 1
test_input_2 = np.array([[[199, 160, 155], [199, 158, 152], [201, 158, 152]],
                  [[202, 167, 163], [202, 165, 159], [200, 163, 157]],
                  [[205, 174, 169], [202, 171, 166], [200, 167, 160]],
                  [[199, 171, 167], [195, 166, 160], [191, 162, 156]],
                  [[200, 159, 155], [197, 156, 150], [196, 155, 149]]],
                 dtype="uint8")

inputImage = Image.fromarray(test_input_2)
inputImage.save("test_imgs/get_image_details/test_input_2.png")

test_input_path_2 = "test_imgs/get_image_details/test_input_2.png"

expexted_detail_2 = {'Aspect Ratio': "3 : 5"}

expected_details_df_2 = pd.DataFrame(expexted_detail_2, index = ['Image'])


def test_input_type():
    '''
    This function tests whether the input file is the right type.
    '''

    with pytest.raises(OSError):
        get_image_details("tests/test_imgs/get_image_details/input.docx", "All")
    with pytest.raises(OSError):
        get_image_details("tests/test_imgs/get_image_details/input.pdf", "All")


def test_non_string_input():
    '''
    This function tests whether the input path is a valid string.
    '''

    with pytest.raises(AttributeError):
        get_image_details(99999999, "All")


def test_nonexistent_input_path():
    '''
    This function tests whether the input path exists.
    '''

    with pytest.raises(FileNotFoundError):
        get_image_details("test_imgs/hello/world.png", "All")


def test_non_string_detail_name():
    '''
    This function tests whether the given detail name is a string.
    '''

    with pytest.raises(KeyError):
        get_image_details(test_input_path_1, 999)


def test_invalid_detail_name():
    '''
    This function tests whether the given detail name string is valid.
    '''

    with pytest.raises(KeyError):
        get_image_details(test_input_path_1, "wrong name")


def test_image_details():
    '''
    This function tests whether get_image_details function returns the right details.
    '''

    test_output_1 = get_image_details(test_input_path_1, "All")
    expected_output_1 = expected_details_df_1
    assert np.array_equal(test_output_1, expected_output_1), "The image_details function does not work properly."

    test_output_2 = get_image_details(test_input_path_2, "Aspect Ratio")
    expected_output_2 = expected_details_df_2
    assert np.array_equal(test_output_2, expected_output_2), "The image_details function does not work properly."
