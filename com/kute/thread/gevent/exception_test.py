#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/1/3 20:33'

"""
gvent 对于异常的处理

"""

from gevent.util import wrap_errors


def func():
    return 3 + 4


def main():
    # 1. 函数异常包装, 如出现异常,返回异常信息(不raise); 否则返回函数执行结果
    wrapfunc = wrap_errors((TypeError, ValueError), func)
    error = wrapfunc()
    print(error)


if __name__ == '__main__':
    main()
