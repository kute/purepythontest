#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/16 20:15'

"""

需要下载  http://code.google.com/p/tesseract-ocr/
 https://sourceforge.net/projects/tesseract-ocr/编译安装

 然后安装  https://github.com/tesseract-ocr/tesseract/wiki


 see   http://stackoverflow.com/questions/38097148/pytesseract-no-such-file-or-directory-error


"""

from pytesseract import image_to_string
from PIL import Image


def main():
    image = Image.open('pin.png')
    ltext= image_to_string(image)
    print(ltext)


if __name__ == '__main__':
    main()
