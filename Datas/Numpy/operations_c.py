import numpy as np

matrix = np.loadtxt("data.txt", delimiter=" ")

print(np.diag(matrix, k=0))

matrix = np.asmatrix(matrix) # interprets input as matrix = np.matrix(matrix, copy=False)
# Equals.
matrix = np.mat(matrix)

amatrix = matrix.copy()

###### Basic ops ######

print(matrix + amatrix) # np.add
print(matrix - amatrix + np.identity(matrix.shape[0])) # np.subtract
print(matrix * amatrix) # Also known as np.dot
# Have np.divide as well.

v = np.array([1, 0, 0])

print(matrix.dot(v))

###### For vectors also ######

v = np.array([1, 2, 3])
w = v.copy()

v += 2

print(np.vdot(v, w))
# Vector dot [1, 2, 3] vdot [3, 4, 5] = 3 + 8 + 15 = 26.
print(amatrix.dot(matrix))
