
# coding: utf-8

# In[4]:


import numpy as np
import skimage.io
import pytest
import matplotlib.image as mpimg
from BeautyPy.flip import flip
# In[13]:


test_input_file_path = "test_imgs/compress/test_input.png"
test_output_file_path = "test_imgs/compress/test_output.png"






def test_flip_same_size():
    '''
    Function to test that the output matrix is correct
    '''
    flip(test_input_file_path,test_output_file_path,"v")
    input_img = skimage.io.imread(test_input_file_path)
    test_output = skimage.io.imread(test_output_file_path)
    assert input_img.shape == test_output.shape,"Input and output shape are not the same"

def test_flip_input_type():
    '''
    Function to test that if the input type is correct.
    If is incorrect, a TypeError is raised

    '''
    with pytest.raises(TypeError):
        flip(image,test_output_file_path,"v")
    with pytest.raises(TypeError):
        flip("test_imgs/emboss/input.pdf",test_output_file_path,"v")
    with pytest.raises(TypeError):
        flip("test_input.jpg",test_output_file_path,"v")

def test_flip_input_shape():
    '''
    Function to test that if the image has correct shape
    '''
    flip(test_input_file_path,test_output_file_path,"v")
    input_img = skimage.io.imread(test_input_file_path)
    assert np.size(input_img.shape) == 3



def test_nonexistent_input_path():
    '''
    Function to test if the input path exists or not
    '''
    with pytest.raises(FileNotFoundError):
        flip("test_imgs/hello/world.png", test_output_file_path,"v")

def test_nonexistent_output_path():
    '''
    Function to test if the output path exists or not
    '''

    with pytest.raises(FileNotFoundError):
        flip(test_input_file_path, "./123/456.jpg","v")

def test_invalid_input():
    '''
    Function to test if the input path is valid
    '''
    with pytest.raises(AttributeError):
        flip(test_input_file_path,test_output_file_path,123)

# Check flip vertically middle column
def test_mid_column_vertical():
    flip(test_input_file_path,test_output_file_path,"v")
    input_img = skimage.io.imread(test_input_file_path)
    test_output = skimage.io.imread(test_output_file_path)
    m,n,d = input_img.shape

    if n % 2 == 0:
        mid = n//2
        assert np.array_equal(input_img[:,mid,:],test_output[:,mid+1,:]),"The middle column is not the same"
    else:
        mid=n//2
        assert np.array_equal(input_img[:,mid,:],test_output[:,mid,:]),"The middle column is not the same"


# Check flip horizentally middle column
def test_mid_column_vertical():
    flip(test_input_file_path,test_output_file_path,"h")
    input_img = skimage.io.imread(test_input_file_path)
    test_output = skimage.io.imread(test_output_file_path)
    m,n,d = input_img.shape

    if n % 2 == 0:
        mid = n//2
        assert np.array_equal(input_img[mid,:,:],test_output[mid+1,:,:]),"The middle row is not the same"
    else:
        mid=n//2
        assert np.array_equal(input_img[mid,:,:],test_output[mid,:,:]),"The middle row is not the same"
