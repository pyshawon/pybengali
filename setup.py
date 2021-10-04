# -*- coding: utf-8 -*-
from setuptools import setup
import setuptools
import io

def readme():
    with io.open('README.rst', encoding='utf8', errors='ignore') as f:
        return f.read()

setup(name='pybengali',
      version='0.0.1',
      description='pybengali is a python3 package for Bengali DateTime and Bengali numeric number conversation and many more',
      long_description=readme(),
      long_description_content_type="text/markdown",
      packages=setuptools.find_packages(),
      install_requires=[],
      classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',		
        'Intended Audience :: Developers',
    		'License :: OSI Approved :: MIT License',
    		'Development Status :: 5 - Production/Stable',
    		'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords=[
        'pybengali', 
        'bengali', 
        'bangla', 
        'bangla date', 
        'bangla digit', 
        'python bangla',
        'python package',
        'python bangla package',
        'python bengali',
        'python bengali date',
        'django bangla date',
        'django bangla',
        'django bengali'
      ],
      python_requires='>=3.6',
      url='https://github.com/pyshawon/pybengali',
      author='Shaid Hasan Shawon',
      author_email='pyshawon@gmail.com',
      license='MIT'
)
