#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/7/31 17:04'

"""
 计算函数执行时间 装饰器

"""


from functools import wraps
import time


def perf_counter(function):
    @wraps(function)
    def _caltime(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()
        print("The function[%s] use total time is %s ms." % (function.__name__, end - start))
        return result
    return _caltime


def process_time(function):
    @wraps(function)
    def _caltime(*args, **kwargs):
        start = time.process_time()
        result = function(*args, **kwargs)
        end = time.process_time()
        print("The function[%s] use total time is %s ms." % (function.__name__, (end - start)))
        return result
    return _caltime
