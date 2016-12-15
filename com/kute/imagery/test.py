#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/11/3 20:48'

"""

http://www.boyter.org/decoding-captchas/

"""

from PIL import Image
from operator import itemgetter
import hashlib
import time


def main():
    file = "captcha.png"
    # file = "captcha.gif"
    # file = "GetValidateCode.png"
    im = Image.open(file)
    im = im.convert("P")
    his = im.histogram()

    values = {}
    # printhistogram(im)
    temp = {}
    im2 = Image.new("P", im.size, 255)
    xlist = list(range(im.size[0]))
    ylist = list(range(im.size[1]))
    for x in xlist:
        for y in ylist:
            pix = im.getpixel((x, y))
            temp[pix] = pix
            if pix in [35]:
                im2.putpixel((x, y), 0)

    # printhistogram(im2)
    inletter = False
    foundletter = False
    letterposition = []
    start = 0
    end = 0
    for x in xlist:
        for y in ylist:
            pixel = im2.getpixel((x, y))
            if pixel != 255:
                inletter = True
        if not foundletter and inletter:
            foundletter = True
            start = x
        if foundletter and not inletter:
            foundletter = False
            end = x
            letterposition.append((start, end))
        inletter = False

    print(letterposition)

    count = 0
    for letter in letterposition:
        m = hashlib.md5()
        im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
        m.update("{}{}".format(time.time(), count))
        im3.save("./%s.gif" % (m.hexdigest()))
        count += 1

    # im.save("result.png")
    im2.save("result.png")


def printhistogram(im):
    his = im.histogram()
    values = {}
    for i in list(range(256)):
        values[i] = his[i]
    # k: 颜色id, v: 对应颜色在图像中的像素个数
    # 0: 黑色, 255 白色
    for k, v in sorted(values.items(), key=itemgetter(1), reverse=True):
        print(k, v)

if __name__ == '__main__':
    main()
