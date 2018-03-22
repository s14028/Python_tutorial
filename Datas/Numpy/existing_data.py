import numpy as np

matrix = np.fromfile("data.csv", sep=",").reshape(3, 3)

matrix = np.fromfunction(lambda i, j: i + j, (3, 3))

np.save("matrix", matrix)
r = np.load("matrix.npy")

matrix = np.loadtxt("data.txt", delimiter=" ")
#first, second = np.loadtxt("data.txt", delimiter=" ", usecols=(0, 2), unpack=True) : usecols = reads only those columns. Unpack = returns not matrix, but vectors.

print(matrix)
