#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/7/28 21:32'

import gevent
from gevent import socket
import time


def printnow(n):
    a = n + time.clock()
    print (a)
    time.sleep(n)
    print (a, "asdf")
    return a


def main():
    urls = ['www.google.com', 'www.example.com', 'www.python.org']
    # jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
    jobs = [gevent.spawn(printnow, n) for n in range(10)]
    gevent.joinall(jobs, timeout=10)
    print ([job.value for job in jobs])


if __name__ == '__main__':
    main()
