import numpy as np
from scipy.misc import imread, imsave

image = imread("image.jpg")
print(image.shape)

matrix_for_image = np.array(
        [
            [1, 0, 0],
            [0, 0.5, 0],
            [0, 0, 0.3]
        ]
    )

image = image.dot(matrix_for_image)

imsave("cat.jpg", image)
