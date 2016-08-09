#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: pooltest.py
@ __mtime__: 2016/7/30 17:50

池(pool)是一个为处理数量变化并且需要限制并发的greenlet而设计的结构。 在需要并行地做很多受限于网络和IO的任务时常常需要用到它。

"""
import gevent
from gevent.pool import Pool

p = Pool(4)

def f(n):
    print("value is %s, pool size is %s" % (n, len(p)))

def main():
    p.map(f, range(10))


if __name__ == "__main__":
    main()
