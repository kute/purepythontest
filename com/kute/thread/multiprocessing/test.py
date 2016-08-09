#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: test.py
@ __mtime__: 2016/7/30 15:23



multiprocessing.Process 类似于 threading.Thread
也有三种创建方式，参加threading.Thread

https://docs.python.org/dev/library/multiprocessing.html

"""
from multiprocessing import Process, Pool
import gevent
from kute.caltime import caltime


def f(num):
    # gevent.sleep(1)
    return num * num


@caltime.process_time
def map(pool):
    return pool.map(f, range(100000), 5)


@caltime.process_time
def imap(pool):
    return [i for i in pool.imap_unordered(f, range(100000), 10)]

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        map(pool)
        imap(pool)
