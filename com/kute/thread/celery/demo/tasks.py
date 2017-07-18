#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/17 22:30'

"""

"""

from __future__ import absolute_import, unicode_literals
from celery import Celery
import time


app = Celery('tasks-app')

# namespace: 表示 setting里的所有配置都应该以kute为前缀
app.config_from_object('setting', namespace='kute')

# update config
app.conf.update(
    timezone='Europe/Oslo'
)


@app.task
def add(x, y):
    time.sleep(5)
    return x + y


@app.task
def multi(x, y):
    time.sleep(2)
    return x * y
