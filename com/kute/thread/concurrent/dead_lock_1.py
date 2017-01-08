#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/1/8 16:36'

"""
wait for each other

"""

import time
from concurrent.futures import ThreadPoolExecutor


def wait_a():
    print("a start at:{}".format(time.clock()))
    time.sleep(1)
    print(b.result())
    return "a"


def wait_b():
    print("b start at:{}".format(time.clock()))
    time.sleep(5)
    print(a.result())
    return "b"


pool = ThreadPoolExecutor(max_workers=2)
a = pool.submit(wait_b)
b = pool.submit(wait_a)


def main():
    pass


if __name__ == '__main__':
    main()
