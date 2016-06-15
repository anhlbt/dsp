# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function

# Matrix Algebra
import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])

u = np.array([6, 2, -3, 5])[np.newaxis, :]
v = np.array([3, 5, -1, 4])[np.newaxis, :]
w = np.array([1, 8, 0, 5])[:, np.newaxis]



print('\nQ1. Matrix Dimensions:\n')

mat_list = [('A', 'A'), 
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'), 
            ('u', 'u'),
            ('w', 'w')]

for mat in ['A', 'B', 'C', 'D', 'u', 'w']:
    print('Matrix {}: {}'.format(mat, eval(mat).shape))


# Q1. Matrix Dimensions:
# 
# Matrix A: (2, 3)
# Matrix B: (2, 2)
# Matrix C: (3, 2)
# Matrix D: (2, 3)
# Matrix u: (1, 4)
# Matrix w: (4, 1)



print('\nQ2. Vector Operations:\n')

alpha = 6

mat_list = [('u + v'  , 'u+v'), 
            ('u - v'  , 'u-v'),
            ('α * u'  , 'alpha*u'),
            ('u • v'  , 'np.inner(u.squeeze(), v.squeeze())'), 
            ('‖ u ‖'  , 'np.linalg.norm(u)')]

for op in mat_list:
    print('Operation {}:'.format(op[0]))
    print('{}\n'.format(eval(op[1])))


# Q2. Vector Operations:
# 
# Operation u + v:
# [[ 9  7 -4  9]]
# 
# Operation u - v:
# [[ 3 -3 -2  1]]
# 
# Operation α * u:
# [[ 36  12 -18  30]]
# 
# Operation u • v:
# 51
# 
# Operation ‖ u ‖:
# 8.60232526704



print('\nQ3. Matrix Operations:\n')

mat_list = [('A + C'     , 'A+C'), 
            ('A - C.T'   , 'A-C.T'),
            ('C.T + 3*D' , 'C.T + 3*D'),
            ('B * A'     , 'np.dot(B, A)'), 
            ('B * A.T'   , 'np.dot(B, A.T)')]

for op in mat_list:
    print('Operation {}:'.format(op[0]))
    try:
        print('{}\n'.format(eval(op[1])))
    except:
        print('not defined\n')


# Q3. Matrix Operations:
# 
# Operation A + C:
# not defined
#
# Operation A - C.T:
# [[-4 -7 -3]
#  [ 3  6  4]]
#
# Operation C.T + 3*D:
# [[14  3  3]
#  [ 2  7  9]]
#
# Operation B * A:
# [[-1 -5 -1]
#  [ 2  7  4]]
#
# Operation B * A.T:
# not defined



print('\nOptional:\n')
        
mat_list = [('B * C'   , 'np.dot(B, C)'), 
            ('C * B'   , 'np.dot(C, B)'),
            ('B**4'    , 'np.linalg.matrix_power(B,4)'),
            ('A * A.T' , 'np.dot(A, A.T)'), 
            ('D.T * D' , 'np.dot(D.T, D)')]

for op in mat_list:
    print('Operation {}:'.format(op[0]))
    try:
        print('{}\n'.format(eval(op[1])))
    except:
        print('not defined\n')


# Optional:
# 
# Operation B * C:
# not defined
#
# Operation C * B:
# [[ 5 -6]
#  [ 9 -8]
#  [ 6 -6]]
#
# Operation B**4:
# [[ 1 -4]
#  [ 0  1]]
#
# Operation A * A.T:
# [[14 28]
#  [28 69]]
#
# Operation D.T * D:
# [[10 -4  0]
#  [-4  8  8]
#  [ 0  8 10]]
