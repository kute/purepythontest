#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: tesrta.py
@ __mtime__: 2016/10/21 11:29

"""


def testfunc(*args, a=1, b=2, c=3, d=4 ):
    print(a, b, c, d)

args = (1, 2, 3, 4)
testfunc(*args, a=10, b=20, c=30, d=40 )


def test2(a=1, b=2, c=3, d=4, *args, **kwargs):
    print(a, b, c, d)

args = (1, 2, 3, 4)
kwargs = {'a': 1, 'b': 2}
test2(a=10, *args, **kwargs)

def main():
    print("hello")


if __name__ == "__main__":
    main()
