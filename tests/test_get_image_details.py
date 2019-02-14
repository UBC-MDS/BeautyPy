import numpy as np
import skimage.io
import pytest
import matplotlib.image as mpimg


test_input_file_path = "test_imgs/calculate_bytes/test_input.jpg"

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


mpimg.imsave(test_input_file_path, test_input)

def test_wrong_file_type():
'''
This function tests whether the input file is a image.
'''

    with pytest.raises(OSError):
        calculate_bytes("test_imgs/calculate_bytes/input.pdf")

def test_non_string_input():
'''
This function tests whether the input path is a valid string.
'''

    with pytest.raises(AttributeError):
        calculate_bytes(989999999999)

def test_nonexistent_input_path():
'''
This function tests whether the input path exists.
'''
    with pytest.raises(FileNotFoundError):
        calculate_bytes("test_imgs/hello/world.jpg")

def test_calculate_bytes():
'''
This function tests whether calculate_bytes function returns the right image size in bytes.
'''
    test_output = calculate_bytes(test_input_file_path)
    expected_output = 10*5*24/8
    assert np.array_equal(test_output, expected_output), "The calculate_bytes function does not work properly."
