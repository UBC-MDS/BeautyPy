#! /usr/bin/env python

import numpy as np
import pytest
import skimage.io
from PIL import Image
from BeautyPy.emboss import emboss

# initiate file paths
test_input_file_path =  "tests/test_imgs/emboss/test_input.png"
test_output_file_path = "tests/test_imgs/emboss/test_output.png"

# prepare test input image array
test_input = np.array([[[199,160,155],[199,158,152],[201,158,152],[202,157,152],[198,159,154],[199,160,155]],
                       [[202,167,163],[202,165,159],[200,163,157],[199,160,153],[200,161,156],[200,161,156]],
                       [[205,174,169],[202,171,166],[200,167,160],[198,165,158],[198,159,154],[198,159,154]],
                       [[199,171,167],[195,166,160],[191,162,156],[190,160,152],[196,155,151],[196,155,151]],
                       [[200,159,155],[197,156,150],[196,155,149],[196,155,149],[194,155,150],[195,156,151]],
                       [[197,156,150],[196,155,149],[196,155,149],[196,155,149],[194,155,150],[196,157,152]]],
                     dtype="uint8")

# save test input image array as a PNG file on computer
inputImage = Image.fromarray(test_input)
inputImage.save(test_input_file_path)

# prepare expected output image array
exp_output = np.array([[[146, 146, 146], [143, 143, 143], [135, 135, 135], [  1,   1,   1]],
                       [[131, 131, 131], [127, 127, 127], [123, 123, 123], [  1,   1,   1]],
                       [[120, 120, 120], [120, 120, 120], [124, 124, 124], [  1,   1,   1]],
                       [[  1,   1,   1], [  1,   1,   1], [  1,   1,   1], [  1,   1,   1]]],
                      dtype="uint8")

def test_input_path_nonexistent():
    with pytest.raises(FileNotFoundError):
        emboss("tests/test_imgs/hello/world.png", test_output_file_path)

def test_input_file_type_wrong():
    with pytest.raises(OSError):
        emboss("tests/test_imgs/emboss/input.pdf", test_output_file_path)

def test_non_string_input():
    with pytest.raises(AttributeError):
        emboss(9899999999, test_output_file_path)

def test_output_path_nonexistent():
    with pytest.raises(FileNotFoundError):
        emboss(test_input_file_path, "tests/test_imgs/hello/world.png")

def test_output_file_type_wrong():
    with pytest.raises(ValueError):
        emboss(test_input_file_path, "tests/test_imgs/emboss/output.ppt")

def test_non_string_output():
    with pytest.raises(ValueError):
        emboss(test_input_file_path, 2384957372628)

def test_emboss():
    emboss(test_input_file_path, test_output_file_path)
    test_output = skimage.io.imread(test_output_file_path)
    assert np.array_equal(test_output, exp_output), "The emboss function does not work properly."
