#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/8/24 21:36'

"""

"""

import signal
import time
import os


def on_siguser1(signalnum, frame):
    print("receive signal-1:{}={}".format(signalnum, frame))


def main():
    pid = os.getpid()
    print("current pid is:{}".format(pid))

    signal.signal(signal.SIGUSR1, on_siguser1)

    time.sleep(5)

    os.kill(pid, signal.SIGUSR1)

    time.sleep(10)


if __name__ == '__main__':
    main()
