#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: testeasylog.py
@ __mtime__: 2016/8/11 18:46

"""

import os
from com.kute.file.file_util import get_dir, get_sub_dir


def main():
    print(get_dir(os.path.dirname(__file__)))
    print(get_sub_dir("image"))


if __name__ == "__main__":
    main()
