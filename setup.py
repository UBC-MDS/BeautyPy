#!/usr/bin/env python
from distutils.core import setup

setup(
    name='BeautyPy',
    version='0.1',
    author='Jessie Yu, Olivia Lin, Gilbert Lei',
    packages=['BeautyPy'],
    license='MIT',
    description='A toolkit for image processing.',
    url = ['https://github.com/UBC-MDS/BeautyPy'],
    download_url = 'na',
    install_requires=['numpy', 'skimage', 'PIL'],
    long_description=open('README.md').read(),
    )
