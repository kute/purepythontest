#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/2/5 20:24'

"""

http://matplotlib.org/users/image_tutorial.html

"""

from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.figure(1)
    img = image.imread('stinkbug.png')
    plt.subplot(2, 1, 1)
    print(img)
    implot = plt.imshow(img)
    plt.subplot(2, 1, 2)
    luimg = img[:, :, 0]
    print(luimg)
    plt.imshow(luimg)
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    main()
