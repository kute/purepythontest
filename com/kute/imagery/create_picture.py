#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
自定义生成图片（随机汉字和随机背景色）
@version: 1.0
@ __author__: longbai 
@ __file__: create_picture.py
@ __mtime__: 2016/6/28 16:21

"""

from PIL import Image, ImageMode, ImageColor, PSDraw, ImageFont, ImageDraw
import random


def main():
    text = ["中", "国", "制", "造"]
    oimg = Image.open("noface80_80.png")
    newimage = Image.new("RGB", oimg.size, random.randint(0, 255))
    size = newimage.size
    font = ImageFont.truetype('simhei.ttf', 45)
    draw = ImageDraw.Draw(newimage)
    draw.text((size[0] * 0.2, size[1] * 0.2), str(text[random.randint(0, len(text) - 1)], "utf-8"), font=font)
    newimage.save("b.png")


if __name__ == "__main__":
    main()
