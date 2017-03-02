#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/2 22:56'

"""

斐波那契计算器


functools.lru_cache : 对于 昂贵的I/O耗费 可以节省时间

maxsize : 最多缓存多少结果
typed: 参数类型不一样是否需要缓存,true为需要


"""

from functools import lru_cache


@lru_cache(maxsize=300, typed=False)
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib2(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    import time
    start = time.clock()
    print(fib(200))
    print(time.clock() - start)
    start = time.clock()
    print(fib2(200))
    print(time.clock() - start)


if __name__ == '__main__':
    main()
