#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: with_mask.py
@ __mtime__: 2017/3/8 15:33

"""

import os
import jieba
from wordcloud import WordCloud
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


basepath = os.path.dirname(__file__)


def main():
    n = 1
    filepath = os.path.join(basepath, 'images/timg{}.jpg'.format(n))
    mask = np.array(Image.open(filepath))

    textfile = os.path.join(basepath, 'sample.txt')
    with open(textfile) as fp:
        text = " ".join(jieba.cut(fp.read(), cut_all=True))
    img = WordCloud(mask=mask).generate(text)

    plt.imshow(img)
    plt.axis('off')
    # plt.imsave(os.path.join(basepath, 'images/figure_{}.png'.format(n)), np.array(img))
    plt.show()


if __name__ == "__main__":
    main()
