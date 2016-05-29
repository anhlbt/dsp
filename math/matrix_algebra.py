#!/usr/bin/env python

# Matrix Algebra
import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])

u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.array([[1], [8], [0], [5]])


print('\nQ1. Matrix Dimensions:\n')

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
for mat in ['u + v', 'u - v', 'alpha*u', 'np.inner(u, v)', 'np.linalg.norm(u)']:
    print('Operation {}: {}'.format(mat, eval(mat)))


# Q2. Vector Operations:
# 
# Operation u + v: [[ 9  7 -4  9]]
# Operation u - v: [[ 3 -3 -2  1]]
# Operation alpha*u: [[ 36  12 -18  30]]
# Operation np.inner(u, v): [[51]]
# Operation np.linalg.norm(u): 8.60232526704


print('\nQ3. Matrix Operations:\n')

for mat in ['A+C', 'A-C.T', 'C.T + 3*D', 'np.dot(B, A)', 'np.dot(B, A.T)']:
    try:
        print('Operation {}: {}'.format(mat, eval(mat)))
    except:
        print('Operation {}: not defined'.format(mat))

# Q3. Matrix Operations:
# 
# Operation A+C: not defined
# Operation A-C.T: [[-4 -7 -3]
#                   [ 3  6  4]]
# Operation C.T + 3*D: [[14  3  3]
#                       [ 2  7  9]]
# Operation np.dot(B, A): [[-1 -5 -1]
#                          [ 2  7  4]]
# Operation np.dot(B, A.T): not defined

print('\nOptional:\n')

for mat in ['np.dot(B, C)', 'np.dot(C, B)', 'np.linalg.matrix_power(B,4)', 'np.dot(A, A.T)', 'np.dot(D.T, D)']:
    try:
        print('Operation {}: {}'.format(mat, eval(mat)))
    except:
        print('Operation {}: not defined'.format(mat))
        

# Optional:
# 
# Operation np.dot(B, C): not defined
# Operation np.dot(C, B): [[ 5 -6]
#                          [ 9 -8]
#                          [ 6 -6]]
# Operation np.linalg.matrix_power(B,4): [[ 1 -4]
#                                         [ 0  1]]
# Operation np.dot(A, A.T): [[14 28]
#                            [28 69]]
# Operation np.dot(D.T, D): [[10 -4  0]
#                            [-4  8  8]
#                            [ 0  8 10]]
