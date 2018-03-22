import numpy as np
####### Creating an array #######
array = np.arange(25).reshape(5, 5)
# arange - array range: creates an 25 element array.
# reshape: changes shape of this array into x row and y column matrix.

array = np.array([[1, 0], [0, 1]])
# arrays creates you an array from list.

arraya = np.empty((5, 5))
# empty array of that shape.
arraya = np.empty_like(array)
# creates empty array with same shape and type.

arraya = np.eye(10)
print(arraya)
arraya = np.identity(10)
print(arraya)

# basically doing same - create identidy array with n.

arraya = np.ones((10, 10))
arraya = np.ones_like(array)
arraya = np.zeros((10, 10))
arraya = np.zeros_like(array)
arraya = np.full((10, 10), 0)
arraya = np.full_like(array, 0)
