#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: synchronous_asynchronous.py
@ __mtime__: 2016/7/29 18:44

"""
import gevent
import random


def task(i):
    sleep = random.randint(0, 10) * 0.001
    gevent.sleep(sleep)
    print( "task done at %s sleep %s" % (i, sleep))


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    tasks = [gevent.spawn(3, task, i) for i in range(1, 10)]
    gevent.joinall(tasks)


if __name__ == "__main__":
    synchronous()

    print ("synchronous done")

    asynchronous()
