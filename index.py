# from keras.datasets import mnist
import numpy as np
#
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
#
#
#
#
#
# print(train_images.ndim)
# print(train_images.shape)
# print(train_images.dtype)



arr = \
[
    [
    [
        [1, 2, 2],
        [1, 2, 3],
        [1, 52, 3]
    ],
    [
        [1, 2, 2],
        [1, 2, 3],
        [1, 533, 3]
    ],
    [
        [1, 2, 2],
        [1, 2, 3],
        [1, 52, 3]
    ],
        ],
    [
        [
            [1, 2, 2],
            [1, 2, 3],
            [1, 52, 3]
        ],
        [
            [1, 2, 2],
            [1, 2, 3],
            [1, 533, 3]
        ],
        [
            [1, 2, 2],
            [1, 2, 3],
            [1, 52, 3]
        ],
    ],
]

print(np.array(arr).shape)





