
# coding: utf-8

# In[4]:


import numpy as np
import skimage.io
import pytest
import matplotlib.image as mpimg


# In[13]:


test_input_file_path = "test_imgs/compress/test_input.jpg"
test_output_file_path = "test_imgs/compress/test_output.jpg"
exp_output_file_path = "test_imgs/compress/exp_output.jpg"



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


# In[14]:


exp_output = np.array([[[199, 160, 155], [199, 158, 152]],
                  [[202, 167, 163], [202, 165, 159]],
                  [[205, 174, 169], [202, 171, 166]],
                  [[199, 171, 167], [195, 166, 160]],
                  [[200, 159, 155], [197, 156, 150]]])
                       
                                              


# In[ ]:


mpimg.imsave(test_input_file_path, test_input)
mpimg.imsave(exp_output_file_path, exp_output)


# In[ ]:


def test_compress():
    '''
    Function to test that the output matrix is correct 
    '''
    compress(test_input_file_path,test_output_file_path)
    test_output = mpimg.imread(test_output_file_path)
    expected_output = mpimg.imread(exp_output_file_path)
    assert np.array_equal(test_ouput, expected_output),"The compress function does not work well"
    
def test_compress_type():
    '''
    Function to test that if an image type is correct. 
    If is incorrect, a TypeError is raised 
    
    '''
    with pytest.raises(TypeError):
        compress(image,test_output_file_path)
    with pytest.raises(TypeError):
        compress("test_imgs/emboss/input.pdf",test_output_file_path)
    with pytest.raises(TypeError):
        compress("test_input.jpg",test_output_file_path)

def test_compress_input_shape():
    '''
    Function to test that if the image has correct shape 
    '''
    assert np.size(test_input.shape) == 3
    
def test_compress_shape():
    '''
    Function to test that if the shape of compressed image is the half of original image's shape
    '''
    assert np.array(compress(test_input_file_path,test_output_file_path).shape)[0:2] == np.ceil(np.array(test_input.shape)[0:2]/2).astype(int)   
    
    
def test_nonexistent_input_path():
    '''
    Function to test if the input path exists or not 
    '''
    with pytest.raises(FileNotFoundError):
        emboss("test_imgs/hello/world.jpg", test_output_file_path)

def test_nonexistent_output_path():
    '''
    Function to test if the output path exists or not
    '''
    
    with pytest.raises(FileNotFoundError):
        emboss(test_input_file_path, "./123/456.jpg")        

    
    
    
    
    

