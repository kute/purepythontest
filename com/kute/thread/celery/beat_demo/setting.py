#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: config.py.py
@ __mtime__: 2017/7/18 19:20

http://docs.celeryproject.org/en/latest/userguide/configuration.html#new-lowercase-settings

"""

from datetime import timedelta
from celery.schedules import crontab


kute_broker_url = [
    "redis://:kuteredis@localhost:6379/0"
]

kute_result_backend = "redis://:kuteredis@localhost:6379/1"

kute_imports = (
    "beat_demo.task1",
    "beat_demo.task2"
)

kute_accept_content = ['json']
kute_task_serializer = 'json'
kute_result_serializer = 'json'

# schedules
kute_beat_schedule = {
    'add-every-30-seconds': {
         'task': 'beat_demo.task1.add',
         'schedule': timedelta(seconds=5),       # 每 5 秒执行一次
         'args': (5, 8)                           # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'beat_demo.task2.multi',
        'schedule': crontab(hour=22, minute=26),   # 每天早上 22 点 26 分执行一次
        'args': (3, 7)                            # 任务函数参数
    }
}
