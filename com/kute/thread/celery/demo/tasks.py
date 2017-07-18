#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/17 22:30'

"""

"""

from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.utils.log import get_task_logger
import time

# 日志记录
logger = get_task_logger(__name__)


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


# bind数据绑定, 通过self 获取上下文
@app.task(bind=True)
def div(self, x, y):
    print('Executing2 task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(self.request))
    logger.info(('Executing task id {0.id}, args: {0.args!r} '
                 'kwargs: {0.kwargs!r}').format(self.request))
    try:
        result = x / y
    except Exception as e:
        # 5s后重试机制
        raise self.retry(exc=e, countdown=5, max_retries=3)
    return result
