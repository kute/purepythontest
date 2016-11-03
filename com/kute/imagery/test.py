#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/11/3 20:48'

"""

http://www.boyter.org/decoding-captchas/

"""

from PIL import Image
from operator import itemgetter


def main():
    file = "captcha.png"
    # file = "captcha.gif"
    # file = "GetValidateCode.png"
    im = Image.open(file)
    im = im.convert("P")
    his = im.histogram()

    values = {}
    for i in list(range(256)):
        values[i] = his[i]
    # k: 颜色id, v: 对应颜色在图像中的像素个数
    # 0: 黑色, 255 白色
    for k, v in sorted(values.items(), key=itemgetter(1), reverse=True):
        print(k, v)
    temp = {}
    im2 = Image.new("P", im.size, 255)
    for x in list(range(im.size[0])):
        for y in list(range(im.size[1])):
            pix = im.getpixel((x, y))
            temp[pix] = pix
            if pix in [35]:
                im2.putpixel((x, y), 0)

    # im.save("result.png")
    im2.save("result.png")


if __name__ == '__main__':
    main()
