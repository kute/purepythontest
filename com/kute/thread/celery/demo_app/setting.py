#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/18 21:56'

"""

"""


# http://docs.celeryproject.org/en/latest/userguide/configuration.html#new-lowercase-settings

kute_broker_url = [
    "redis://:kuteredis@localhost:6379/0"
]

kute_result_backend = "redis://:kuteredis@localhost:6379/1"

kute_imports = (
    "demo_app.task1",
    "demo_app.task2"
)

kute_accept_content = ['json']
kute_task_serializer = 'json'
kute_result_serializer = 'json'
kute_timezone = 'Asia/Shanghai'
