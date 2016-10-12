#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: common.py
@ __mtime__: 2016/10/9 17:58

"""

import werkzeug
from werkzeug.test import create_environ


class CommonRequest(object):
    def __init__(self):
        pass


def main():
    print("hello")
    environ = create_environ()


if __name__ == "__main__":
    main()
