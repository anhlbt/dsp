#!/usr/bin/env python

# Matrix Algebra
import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])

u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.array([1, 8, 0, 5])


print('\nQ1. Matrix Dimensions:\n')

for mat in ['A', 'B', 'C', 'D', 'u', 'w']:
    print('Matrix {}: {}'.format(mat, eval(mat).shape))


print('\nQ2. Vector Operations:\n')

alpha = 6
for mat in ['u + v', 'u - v', 'alpha*u', 'np.dot(u, v.T)', 'np.linalg.norm(u)']:
    print('Operation {}: {}'.format(mat, eval(mat)))


print('\nQ3. Matrix Operations:\n')

for mat in ['A+C', 'A-C.T', 'C.T + 3*D', 'np.dot(B, A)', 'np.dot(B, A.T)']:
    try:
        print('Operation {}: {}'.format(mat, eval(mat)))
    except:
        print('Operation {}: not defined'.format(mat))


print('\nOptional:\n')

for mat in ['np.dot(B, C)', 'np.dot(C, B)', 'np.linalg.matrix_power(B,4)', 'np.dot(A, A.T)', 'np.dot(D.T, D)']:
    try:
        print('Operation {}: {}'.format(mat, eval(mat)))
    except:
        print('Operation {}: not defined'.format(mat))