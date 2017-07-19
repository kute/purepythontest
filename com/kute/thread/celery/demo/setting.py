#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: config.py.py
@ __mtime__: 2017/7/18 19:20

"""

from kombu import Queue

# http://docs.celeryproject.org/en/latest/userguide/configuration.html#new-lowercase-settings

kute_broker_url = [
    "redis://:kuteredis@localhost:6379/0"
]

kute_result_backend = "redis://:kuteredis@localhost:6379/1"

kute_imports = (
    "tasks",
)

kute_accept_content = ['json']
kute_task_serializer = 'json'
kute_result_serializer = 'json'

# 定义队列
kute_task_queues = (
    Queue('default', routing_key='task.#'),  # 路由键以“task.”开头的消息都进default队列
    Queue('web_tasks', routing_key='web.#'),  # 路由键以“web.”开头的消息都进web_tasks队列
)
