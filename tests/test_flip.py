
# coding: utf-8

# In[4]:


import numpy as np
import skimage.io
import pytest
from PIL import Image
from BeautyPy.flip import flip

# In[13]:


test_input_file_path = "test_imgs/flip/test_input.png"
test_output_file_path = "test_imgs/flip/test_output.png"

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

    Test that if the input type is correct.


    '''

    with pytest.raises(OSError):
        flip("test_imgs/emboss/input.pdf",test_output_file_path,"v")
    with pytest.raises(OSError):
        flip("test_input.jpg",test_output_file_path,"v")

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
        flip("test_imgs/hello/world.png", test_output_file_path,"v")

def test_nonexistent_output_path():
    '''

    Test if the output path exists or not

    '''

    with pytest.raises(FileNotFoundError):
        flip(test_input_file_path, "./123/456.jpg","v")

def test_invalid_input():
    '''

    Test if the input path is valid

    '''
    with pytest.raises(AssertionError):
        flip(test_input_file_path,test_output_file_path,"123")

# Check flip horizentally middle column
def test_mid_column_horizental():
    flip(test_input_file_path,test_output_file_path,"h")
    input_img = skimage.io.imread(test_input_file_path)
    test_output = skimage.io.imread(test_output_file_path)
    m,n,d = input_img.shape

    if n % 2 == 0:
        mid = n//2
        assert np.array_equal(input_img[:,mid,:],test_output[:,mid-1,:]),"The middle column is not the same"
    else:
        mid=n//2
        assert np.array_equal(input_img[:,mid,:],test_output[:,mid,:]),"The middle column is not the same"


# Check flip vertically middle column
def test_mid_column_vertical():
    flip(test_input_file_path,test_output_file_path,"v")
    input_img = skimage.io.imread(test_input_file_path)
    test_output = skimage.io.imread(test_output_file_path)
    m,n,d = input_img.shape

    if n % 2 == 0:
        mid = n//2
        assert np.array_equal(input_img[mid,:,:],test_output[mid-1,:,:]),"The middle row is not the same"
    else:
        mid=n//2
        assert np.array_equal(input_img[mid,:,:],test_output[mid,:,:]),"The middle row is not the same"
