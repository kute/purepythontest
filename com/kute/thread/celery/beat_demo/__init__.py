#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/18 22:14'

"""

定时任务

1. 在 celery目录下执行: celery worker -A beat_demo -l info
2. 新打开一个terminal在celery 下执行:  celery beat -A beat_demo


或者以上两步合为一步: celery worker -B -A beat_demo -l info

"""


from celery import Celery


app = Celery('beat_demo')
app.config_from_object('beat_demo.setting', namespace='kute')
