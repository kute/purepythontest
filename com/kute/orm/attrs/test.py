#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: test.py
@ __mtime__: 2016/10/21 16:48

"""

import attr


@attr.s
class Person(object):
    name = attr.ib()
    age = attr.ib(default=18)


def main():
    p = Person(name="kute", age=16)
    print(p)


if __name__ == "__main__":
    main()
