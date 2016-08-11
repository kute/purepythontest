#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: testeasylog.py
@ __mtime__: 2016/8/11 18:46

"""


from kute.easylog.easylog import geteasylog


easylog = geteasylog()


def main():
    easylog.info("test easylog info.")
    easylog.warn("test easylog warn")


if __name__ == "__main__":
    main()
