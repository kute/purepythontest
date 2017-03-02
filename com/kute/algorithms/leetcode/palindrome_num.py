#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/2/17 16:50'

"""
回文数
"""


def ispalindrome(x):
    y = str(x)
    ry = y[::-1]
    return y == ry


def main():
    result = ispalindrome(121)
    print(result)


if __name__ == '__main__':
    main()
