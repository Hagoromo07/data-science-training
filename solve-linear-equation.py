import numpy as np

"""
    SOLVING EQUATIONS IN NUMPY
    | 2x + y = 4
    | x + -y = -1

"""

A = np.array([[2, 1], [1, -1]])
B = np.array([4, -1])

C = np.linalg.inv(A)  # inverse of matrix A
print(C)

S = np.dot(C, B)  # dot product of C and B
print(S)
