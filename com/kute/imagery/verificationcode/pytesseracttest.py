#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/2/16 20:15'

"""

需要下载  http://code.google.com/p/tesseract-ocr/
 https://sourceforge.net/projects/tesseract-ocr/编译安装

 然后安装  https://github.com/tesseract-ocr/tesseract/wiki


 see   http://stackoverflow.com/questions/38097148/pytesseract-no-such-file-or-directory-error


"""

from pytesseract import image_to_string
from PIL import Image


from PIL import Image, ImageEnhance, ImageFilter
import pytesseract


def main():
    # 灰度 rgb
    im = Image.open("bVx1uu.jpg").convert('L').convert('RGB')
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save('pin.temp.jpg')
    text = pytesseract.image_to_string(Image.open('pin.temp.jpg'))
    print(text)


if __name__ == '__main__':
    main()
