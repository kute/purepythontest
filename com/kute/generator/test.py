#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/1/11 21:13'

"""
测试单例 生成器
"""

from kute.singleton.singleton import singleton
from collections import defaultdict


@singleton
class MyClass(object):
    pass


def main():
    m1 = MyClass()
    m2 = MyClass()
    print(m1 == m2)

    d = {}
    c = d.fromkeys(range(5), [])

    d = defaultdict(list)
    d[0].append(9)
    print(d[0])
    print(d[1])


if __name__ == '__main__':
    main()
