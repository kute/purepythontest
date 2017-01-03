#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/7/28 21:32'

import gevent
import random
from gevent import socket
import time
import gevent


def task1():
    print('task1 begin')
    gevent.sleep(4)
    print('task1 end')


def task2():
    print('task2 begin')
    gevent.sleep(2)
    print('task2 end')


def main():
    tasks = [gevent.spawn(task1), gevent.spawn(task2)]
    results = gevent.joinall(tasks)
    print(results)


if __name__ == '__main__':
    main()
