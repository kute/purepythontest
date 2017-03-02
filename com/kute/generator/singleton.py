#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/1/11 21:07'

"""
单例装饰器
在类上使用
单例的其他形式:
https://github.com/taizilongxu/interview_python#16-%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F
"""


def singleton(cls, *args, **kw):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance
