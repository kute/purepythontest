#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/17 21:16'

"""

检测图片类型

"""

import imghdr
import os
from com.kute.file.pathlib.fileutil import FileUtil


# _resources_dir = os.path.join(os.path.dirname(__file__), "resources")
#
#
# def getfilepath(filename):
#     return os.path.join(_resources_dir, filename)


def main():
    # filepath = getfilepath("a.jpg")
    filepath = FileUtil.getfilepath(FileUtil.IMAGE, "a.jpg")
    print(filepath)
    print(imghdr.what(filepath))


if __name__ == '__main__':
    main()
