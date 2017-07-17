#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/17 22:42'

"""

"""

from .demo import add


def main():
    print('main begin')
    add.delay(4, 9)
    print('main end')


if __name__ == '__main__':
    main()
