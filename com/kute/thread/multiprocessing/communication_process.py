#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: communication_process.py
@ __mtime__: 2016/12/29 10:53

进程间通信

"""

import multiprocessing
from multiprocessing import Queue, Process, Pool, Value, Array, sharedctypes


def childfunc(queue):
    queue.put("32")


def child_pip(child_conn):
    child_conn.send([23, '23423'])
    print("child pip process get data:{}".format(child_conn.recv()))
    child_conn.close()


def child_share(v, a):
    v.value = 3.1415926
    for i in list(range(len(a))):
        a[i] = -a[i]


def main():
    # 1. 父进程与子进程通信（不使用pool），则可以直接用 multiprocessing.Queue队列
    queue = Queue()
    p = Process(target=childfunc, args=(queue, ), name="child-process")
    p.start()
    p.join()
    print("parent process get data:{}".format(queue.get()))

    # 2. 父进程与子进程通信（使用pool），则不能使用 multiprocessing.Queue队列，应使用 multiprocessing.Manager().Queue()
    queue = multiprocessing.Manager().Queue()
    pool = Pool()
    pool.apply(childfunc, args=(queue, ))
    print("parent process get data:{}".format(queue.get()))

    # 3. 通信还可以使用 Pipe()，代表 一个通信（connection）的两端, duplex双工
    parent, child = multiprocessing.Pipe(duplex=True)
    p = Process(target=child_pip, args=(child, ))
    parent.send('parent info')
    p.start()
    p.join()
    print("parent process get data:{}".format(parent.recv()))

    # 4. 使用 Value 或者 Array 来存储共享内容（可被任意修改）
    v = Value("d", 0.0)
    a = Array("i", list(range(10)))
    p = Process(target=child_share, args=(v, a))
    p.start()
    p.join()
    print("parent get shared data:{}={}".format(v.value, a[:]))


if __name__ == "__main__":
    main()
