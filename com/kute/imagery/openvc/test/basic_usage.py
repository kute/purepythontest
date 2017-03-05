#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/5 18:47'

"""

"""

import cv2
from PIL import Image


def baseinfo(filename):
    img = cv2.imread(filename)
    print(img.shape)  # 灰度图不会返回第三列
    print(img.size)  # 像素数目
    print(img.dtype)

    # 获取某个像素点
    print(img[200, 200, 0])
    print(img.item(10, 10, 0))  # better this way

    # img.itemset((10, 10, 0), 0)  # 设置某个像素点
    # img[10: 200, 10: 200, :] = 125  # 像素区域设置

    b, g, r = cv2.split(img)  # 拆分与合并BGR通道
    img = cv2.merge((b, g, r))

    # 图像混合公式: dst = α · img1 + β · img2 + γ
    img2 = cv2.imread('images/stinkbug.png')
    img = cv2.resize(img, Image.open('images/stinkbug.png').size, interpolation=cv2.INTER_CUBIC)
    img12 = cv2.addWeighted(img, 0.4, img2, 0.6, 5)

    cv2.imshow('window', img12)
    destroy()


def bitwise_test():
    img = cv2.imread('images/girl.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print(gray)
    _, mask = cv2.threshold(gray, 172, 255, cv2.THRESH_BINARY)
    print(mask)
    maskinv = cv2.bitwise_not(gray, mask=mask)
    print(maskinv)

    cv2.imshow('window', mask)
    destroy()


def destroy():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    filename = 'images/a.jpg'
    # baseinfo(filename)
    bitwise_test()


if __name__ == '__main__':
    main()
