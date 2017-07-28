#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: download_utils.py
@ __mtime__: 2017/7/28 9:59

Utilities for file download and caching.

"""

from keras.utils.data_utils import get_file


def main():
    targetdir = "E:\\download\\hehe.whl"
    origin = "https://pypi.python.org/packages/b4/20/e5bc57a8df0cb98a800cead0b8c9538f795706fa51c65e05ee4906f693af/numpy-1.13.1-cp34-cp34m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl#md5=3eee3605dd61f02583264eb5697d8207"
    path = get_file(targetdir, origin, untar=False)
    print(path)


if __name__ == "__main__":
    main()
