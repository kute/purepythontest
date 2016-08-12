#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: logformat.py
@ __mtime__: 2016/8/12 19:07

"""

from logbook import StreamHandler, info
import sys


StreamHandler(sys.stdout).push_application()


def main():
    info("test")


if __name__ == "__main__":
    main()
