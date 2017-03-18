#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: test.py
@ __mtime__: 2017/2/8 15:18

这里测试说明  codecs.open

"""

import codecs


def main():
    with codecs.open('read.txt', 'r', 'utf-8') as rfile:
        content = rfile.read()
        print(content)
        print(type(content))


if __name__ == "__main__":
    main()
