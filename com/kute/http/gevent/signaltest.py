#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: signaltest.py
@ __mtime__: 2016/7/30 17:33

"""


import gevent
import signal


def run_forever():
    gevent.sleep(100000)


def main():
    gevent.signal(signal.SIGQUIT, gevent.shutdown)
    thread = gevent.spawn(run_forever)
    thread.join()


if __name__ == "__main__":
    main()
