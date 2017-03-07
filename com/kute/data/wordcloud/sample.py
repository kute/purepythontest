#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/7 22:09'

"""

"""

import os
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

basepath = os.path.dirname(__file__)


def main():
    with open(os.path.join(basepath, 'sample.txt')) as fp:
        # from file
        img = WordCloud().generate(fp.read())

    plt.figure(1)
    plt.subplot(3, 1, 1)
    plt.imshow(img)
    plt.axis('off')

    # from text
    text = "today is a good day"
    img = WordCloud().generate_from_text(text)
    plt.subplot(3, 1, 2)
    plt.imshow(img)
    plt.axis('off')

    # custom
    mask = np.array(Image.open(os.path.join(basepath, 'stinkbug.png')))
    text = open(os.path.join(basepath, 'a.txt')).read()
    plt.figure(2)
    # plt.subplot(3, 1, 3)
    img = WordCloud(max_words=400, mask=mask, width=600, height=800, margin=10).generate(text)
    plt.imshow(img)
    plt.axis('off')

    plt.show()


if __name__ == '__main__':
    main()
