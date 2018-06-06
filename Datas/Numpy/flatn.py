import numpy as np

array = np.array([[1, 2], [3, 4]])
array = array.flatten()
print(array)
#Works all the times
array = np.array([['A', 'B'], ['D', 'W']])
array = np.hstack(array)
print(array)
