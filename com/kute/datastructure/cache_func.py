#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/2 22:56'

"""

斐波那契计算器


functools.lru_cache : 对于 昂贵的I/O耗费 可以节省时间

https://docs.python.org/3.6/library/functools.html#functools.lru_cache

maxsize : 最多缓存多少结果
typed: 参数类型不一样是否需要缓存,true为需要


"""

from functools import lru_cache, wraps


@lru_cache(maxsize=300, typed=False)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib2(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def cachefunc(fn):
    cache = {}

    @wraps(fn)
    def cachefunc(*args, **kwargs):
        if args not in cache:
            cache[args] = fn(*args, **kwargs)
        return cache[args]
    return cachefunc


@cachefunc
def fib3(n):
    """python 3.2之前使用cache func的形式
    """
    if n < 2:
        return n
    return fib3(n - 1) + fib3(n - 2)


def main():
    import time
    start = time.clock()
    print("结果:{}, 用时:{}".format(fib(200), time.clock() - start))
    start = time.clock()
    print("结果:{}, 用时:{}".format(fib2(200), time.clock() - start))
    start = time.clock()
    print("结果:{}, 用时:{}".format(fib3(200), time.clock() - start))

    print("缓存信息fib1:{}".format(fib.cache_info()))


if __name__ == '__main__':
    main()
