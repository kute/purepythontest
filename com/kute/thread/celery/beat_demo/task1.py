#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/18 21:58'

"""

"""

import time
from beat_demo import app


@app.task
def add(x, y):
    time.sleep(5)
    return x + y
