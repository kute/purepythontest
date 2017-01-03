#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
并行 请求

多线程对多个不通的数据的并发访问
对同一个数据的话，可以先构造多个相同的数据再处理
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
import multiprocessing
import time

monkey.patch_all()


def main():
    # urls = ["https://www.baidu.com/"] * 100
    urls = []
    for i in range(10):
        urls.append("https://www.baidu.com/s?wd={}".format(i))
    pool = Pool(20)
    print("start............................................")
    pool.map(get, urls)  # 阻塞调用，会等待所有的结果完成后 方法才会全部返回
    print("end ............................................map")
    result = pool.map_async(get, urls)  # 非阻塞，方法立即返回，但是只有在调用 get 才会返回结果
    print("end.............................................map_async")
    pool.join()
    result.get()
    print("end..............................................")


def get(url):
    print("{}=={}=={}".format(url, requests.get(url).status_code, multiprocessing.current_process().name))
    time.sleep(1)
    return url


if __name__ == "__main__":
    main()
