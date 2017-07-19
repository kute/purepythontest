#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/18 21:59'

"""

1. 在 celery目录下首先执行: celery worker -A demo_app -l info
2. 然后新打开一个terminal执行: python demo_app_client.py

"""

from datetime import datetime, timedelta
from demo_app import task1
from demo_app import task2


# countdown: n秒后开始执行
# expires: 任务过期时间
# http://docs.celeryproject.org/en/latest/reference/celery.app.task.html#celery.app.task.Task.apply_async
task1.add.apply_async(args=[2, 8], countdown=3, expires=4)

# eta: 指定任务被调度的具体时间(datetime类型)
task2.multi.apply_async(args=[3, 7], eta=datetime.utcnow() + timedelta(seconds=10))


print('hello world')
