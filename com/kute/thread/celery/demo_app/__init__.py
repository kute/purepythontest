#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/18 21:55'

"""

"""


from celery import Celery


app = Celery('demo_app')
app.config_from_object('demo_app.setting', namespace='kute')
