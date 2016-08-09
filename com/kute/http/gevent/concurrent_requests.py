#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
并行 请求
Spawn multiple workers and wait for them to complete
@version: 1.0
@ __author__: longbai 
@ __file__: concurrent_requests.py
@ __mtime__: 2016/7/29 16:17

"""

import gevent
from gevent import monkey
from gevent.pool import Pool
import requests
import threading

monkey.patch_all()


def main():
    urls = ["https://www.baidu.com/"] * 100
    pool = Pool(20)
    print( pool.map(get, urls))


def get(url):
    return requests.get(url=url).status_code


if __name__ == "__main__":
    main()
