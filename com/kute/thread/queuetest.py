#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: queuetest.py
@ __mtime__: 2016/7/1 18:16

"""

# from Queue import Queue
import time

def main():
    # queue = Queue(10)
    # for i in range(10):
    #     queue.put(i)
    #     print time.ctime()
    # try:
    #     while 1:
    #         data = get(queue)
    #         print data, queue.qsize()
    #         if data > 12:
    #             break
    # except Exception as e:
    #     print "timeout"
    pass


def get(queue):
    return queue.get(True, 2)


def put(queue, i):
    queue.put(True, 2)


if __name__ == "__main__":
    main()
