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

1. 进程的启动方式有三种：(multiprocessing.set_start_method())
  spawn: 子进程只会继承运行时必要的资源，非必要的不会继承，相对于其他启动方式 较慢。
  fork : 子进程会全部继承父进程的所有资源
  forkserver: 启动时，父进程 连接到 server 然后请求创建一个新的进程（新进程是单线程的，所以线程安全）

"""
import multiprocessing
from multiprocessing import Process, Pool
import gevent
from kute.caltime import caltime


def f(num):
    # gevent.sleep(1)
    return num * num


@caltime.process_time
def map(pool):
    multiprocessing.get_context().set_start_method("fork")
    return pool.map(f, range(100000), 5)


@caltime.process_time
def imap(pool):
    return [i for i in pool.imap_unordered(f, range(100000), 10)]

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        map(pool)
        imap(pool)
