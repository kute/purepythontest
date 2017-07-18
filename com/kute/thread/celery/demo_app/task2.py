#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/18 21:58'

"""

"""

import time
from demo_app import app


@app.task
def multi(x, y):
    time.sleep(3)
    return x * y
