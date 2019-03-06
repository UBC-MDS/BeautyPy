#! /usr/bin/env python

import numpy as np
import pandas as pd
import skimage.io
import pytest
from PIL import Image
from BeautyPy.get_image_details import get_image_details

test_input_file_path =  "tests/test_imgs/get_image_details/test_input.png"

test_input = np.array([[[199, 160, 155], [199, 158, 152], [201, 158, 152], [202, 157, 152], [198, 159, 154]],
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


inputImage = Image.fromarray(test_input)
inputImage.save(test_input_file_path)

expexted_detail = {'Dimension': "5 x 10", 'Width': 5, 'Height': 10, 'Aspect Ratio': "1 : 2"}

expected_details_df = pd.DataFrame(expexted_detail, index = ['Image'])


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
        get_image_details("tests/test_imgs/hello/world.png", "All")


def test_non_string_detail_name():
    '''
    This function tests whether the given detail name is a string.
    '''

    with pytest.raises(KeyError):
        get_image_details(test_input_file_path, 999)


def test_invalid_detail_name():
    '''
    This function tests whether the given detail name string is valid.
    '''

    with pytest.raises(KeyError):
        get_image_details(test_input_file_path, "wrong name")


def test_image_details():
    '''
    This function tests whether get_image_details function returns the right details.
    '''

    test_output = get_image_details(test_input_file_path, "All")
    expected_output = expected_details_df
    assert np.array_equal(test_output, expected_output), "The image_details function does not work properly."
