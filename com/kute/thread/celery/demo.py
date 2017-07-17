#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/17 22:30'

"""

"""

import time
from celery import Celery


app = Celery('tasks', broker='redis://:kuteredis@localhost:6379', backend='redis://:kuteredis@localhost:6379/0')


@app.task
def add(x, y):
    time.sleep(5)
    return x + y


if __name__ == '__main__':
    print('main')
    add(4, 7)
    print('end')
