#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: config.py.py
@ __mtime__: 2017/7/18 19:20

"""

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
