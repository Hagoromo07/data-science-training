import numpy as np

"""
    BROADCASTING IN NUMPY
    
    Perform arithmetic operations on different shaped arrays
    smaller array is broadcast across the larger array to ensure shape consistency
    
    Rule: 
    * one dimension (either column or row ) should have the same dimensions for both arrays
    * The lower dimension array should be an 1D array

"""

A = np.arange(20).reshape(5, 4)

print(A)
print(type(A))  # <class 'numpy.ndarray'>

B = np.arange(5).reshape(5, 1)

print(B + A)
