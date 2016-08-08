#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/7/31 17:44'

"""

"""

from kute.caltime.caltime import perf_counter


@perf_counter
def test(a):
    print([i for i in range(1, a)])
    return "ok"


if __name__ == '__main__':
    print(test(10000))
