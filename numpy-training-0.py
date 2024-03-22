import numpy as np

"""
    Numpy is a an dimensional array object or ndarray,
    which provide a fast and efficient way of storing homogenous data.
    we can have ndarray with 1 dimension or 1 row and these are rank 1 arrays
    
    or we can have multi-dimensional arrays with more than one row [[row1, row2], [row3, row4]]
"""

# rank 1 array
arr1 = [3, 4, 5, 6, 7]

print(type(arr1))  # <class 'list'>

arr2 = np.array(arr1)
print(type(arr2))  # <class 'numpy.ndarray'>

# multi-dimensional array
arr3 = [[3, 4, 5], [6, 7, 8], [9, 10, 11]]
arr4 = np.array(arr3)
print(arr4)


"""
==================================
|                                |
| Matrix arithmetics and algebra |
|                                |
==================================

* dot product of two vectors is a scalar, i.e a single number
* It carries out element-wise multiplication and it output is a vector
* Matrix operator
    M(2x3) * M(3x2) = M(2x2)
    M(2x2) + M(2x2) = M(2x2)
* Matrix division
    Matrix A / Matrix B = Matrix A * Inverse of Matrix B
    
* Vector arithmetics
    Vector A +/- Vector B = Vector C
    Vector A * Vector B = Scalar
    Vector A / Vector B = Scalar
"""

y = np.array([1, 2, 3, 4, 5])
x = np.array([6, 7, 8, 9, 10])

# addition, subtract
print(x + y)  # [ 7  9 11 13 15]
print(x - y)  # [ 5  5  5  5  5]

# scalar
print(x * 2)  # [12 14 16 18 20]

# dot product
print(x * y)  # [ 6 14 24 36 50]

