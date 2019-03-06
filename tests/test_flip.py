
# coding: utf-8

# In[4]:


import numpy as np
import skimage.io
import pytest
from PIL import Image
from BeautyPy.flip import flip

# In[13]:


test_input_file_path =  "tests/test_imgs/flip/test_input.png"
test_output_file_path = "tests/test_imgs/flip/test_output.png"

test_input = np.array([[[199,160,155],[199,158,152],[201,158,152]],
                       [[202,167,163],[202,165,159],[200,163,157]],
                       [[205,174,169],[202,171,166],[200,167,160]],
                       [[199,171,167],[195,166,160],[191,162,156]],
                       [[200,159,155],[197,156,150],[196,155,149]],
                       [[197,156,150],[196,155,149],[196,155,149]]],
                     dtype="uint8")

# save test  input image array as a PNG file on computer
inputImage = Image.fromarray(test_input)
inputImage.save(test_input_file_path)

exp_output_h = np.array([[[201, 158, 152],[199, 158, 152],[199, 160, 155]],
                         [[200, 163, 157],[202, 165, 159],[202, 167, 163]],
                         [[200, 167, 160],[202, 171, 166],[205, 174, 169]],
                         [[191, 162, 156],[195, 166, 160],[199, 171, 167]],
                         [[196, 155, 149],[197, 156, 150],[200, 159, 155]],
                         [[196, 155, 149],[196, 155, 149],[197, 156, 150]]], dtype="uint8")

exp_output_v = np.array([[[197, 156, 150],[196, 155, 149],[196, 155, 149]],
                         [[200, 159, 155],[197, 156, 150],[196, 155, 149]],
                         [[199, 171, 167],[195, 166, 160],[191, 162, 156]],
                         [[205, 174, 169],[202, 171, 166],[200, 167, 160]],
                         [[202, 167, 163],[202, 165, 159],[200, 163, 157]],
                         [[199, 160, 155],[199, 158, 152],[201, 158, 152]]], dtype="uint8")

def test_flip_v():
    flip(test_input_file_path, test_output_file_path,"v")
    test_output_v = skimage.io.imread(test_output_file_path)
    assert np.array_equal(test_output_v, exp_output_v), "The flip function does not work properly."

def test_flip_h():
    flip(test_input_file_path, test_output_file_path,"h")
    test_output_h = skimage.io.imread(test_output_file_path)
    assert np.array_equal(test_output_h, exp_output_h), "The flip function does not work properly."



def test_flip_same_size():
    '''

    Test that the output size is correct

    '''
    flip(test_input_file_path,test_output_file_path,"v")
    input_img = skimage.io.imread(test_input_file_path)
    test_output = skimage.io.imread(test_output_file_path)
    assert input_img.shape == test_output.shape,"Input and output shape are not the same"

def test_flip_input_type():
    '''

    Test that if the input type is png.


    '''

    with pytest.raises(OSError):
        flip("tests/test_imgs/emboss/input.pdf",test_output_file_path,"v")
    with pytest.raises(OSError):
        flip("test_input.jpg",test_output_file_path,"v")

def test_flip_input_string():
    '''

    Test that if the input is string.

    '''
    with pytest.raises(AttributeError):
        flip(123,test_output_file_path,"v")

def test_flip_output_string():
    '''

    Test that if the output is string.

    '''
    with pytest.raises(ValueError):
        flip(test_input_file_path,123,"v")

def test_flip_input_shape():
    '''

    Test that if the image has correct shape

    '''
    flip(test_input_file_path,test_output_file_path,"v")
    input_img = skimage.io.imread(test_input_file_path)
    assert np.size(input_img.shape) == 3



def test_nonexistent_input_path():
    '''

    Test if the input path exists or not

    '''
    with pytest.raises(FileNotFoundError):
        flip("tests/test_imgs/hello/world.png", test_output_file_path,"v")

def test_nonexistent_output_path():
    '''

    Test if the output path exists or not

    '''

    with pytest.raises(FileNotFoundError):
        flip(test_input_file_path, "./123/456.jpg","v")

def test_invalid_input():
    '''

    Test if the input direction is valid

    '''
    with pytest.raises(AssertionError):
        flip(test_input_file_path,test_output_file_path,"123")
