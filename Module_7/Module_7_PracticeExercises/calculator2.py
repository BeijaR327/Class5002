# -*- coding: utf-8 -*-

""" Calculator program from 
https://physicalmodelingwithpython.blogspot.com/2015/09/speeding-up-python-part-1-profiling.html

"""

# -----------------------------------------------------------------------------
# calculator.py
# ----------------------------------------------------------------------------- 

#storage is numpy, but calculations use loops
# not efficient, mean to illustrate the issues

import numpy as np

def add(x, y):
    """
    Add two arrays using NumPy's vectorized operation.
    x and y must be two-dimensional arrays of the same shape.
    """
    return x + y

def multiply(x, y):
    """
    Multiply two arrays using NumPy's vectorized operation.
    x and y must be two-dimensional arrays of the same shape.
    """
    return x * y

def sqrt(x):
    """
    Take the square root of the elements of an array using NumPy.
    """
    return np.sqrt(x)

def hypotenuse(x, y):
    """
    Return sqrt(x**2 + y**2) for two arrays, x and y.
    x and y must be two-dimensional arrays of the same shape.
    """
    return np.sqrt(x**2 + y**2)
