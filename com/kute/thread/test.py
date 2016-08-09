#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: test.py
@ __mtime__: 2016/7/1 16:41

"""

import time
from threading import Thread


class Th(Thread):
    def run(self):
        time.sleep(2)
        print "sleep-%s-%s" % (self.getName(), self.ident)

    def __init__(self, name=None):
        Thread.__init__(self, name=name)
        self.name = name


def method_2():
    print "begin"
    for i in range(1, 10):
        t = Th("testthread-%s" % i)
        t.setDaemon(True)
        t.start()
        t.join()
    print "end"


def dowork(i):
    # time.sleep(5)
    print "current num is %d" % i
    print


def method_1():
    for i in range(1, 10):
        t = Thread(target=dowork, args=(i,))
        t.start()
        t.join()


class Callable(object):
    def __init__(self, func, args):
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)


def method_3():
    for i in range(1, 10):
        t = Thread(target=Callable(dowork, (i, )))
        t.start()
        t.join()

# 三种方式创建
if __name__ == "__main__":
    # 传递函数与参数
    # method_1()
    # 继承Thread类，实现run
    # method_2()
    # 传入可调用对象
    method_3()
