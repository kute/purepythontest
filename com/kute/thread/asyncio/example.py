#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/1/8 21:31'

"""

"""

import asyncio
import time
import datetime
import functools


async def hello():
    print("hello")
    time.sleep(5)  # 模拟耗时操作
    print("hello after 5 seconds")


def test_run_until_complete():
    loop = asyncio.get_event_loop()
    print("main start")
    loop.run_until_complete(hello())
    print("main continue")
    loop.close()
    print("main end")


def print_current_date(endtime, loop):
    print(datetime.datetime.now())
    if loop.time() + 1 < endtime:
        # 用 functools.partial 使用 命名参数
        loop.call_later(1, functools.partial(print_current_date, endtime=endtime, loop=loop))
        # loop.call_later(1, print_current_date, endtime, loop)
    else:
        loop.stop()


def test_call_later():
    loop = asyncio.get_event_loop()
    endtime = loop.time() + 5
    loop.call_soon(print_current_date, endtime, loop)
    print("")
    loop.run_forever()
    print('2')
    loop.close()


async def compute(x, y):
    print("Compute {} + {} at {}".format(x, y, time.time()))
    # 遇到 await, 当前程序(compute)挂起, 等待 asyncio.sleep 结束
    await asyncio.sleep(3.0)
    print("continue at {}".format(time.time()))
    return x + y

async def print_sum(x, y):
    print("print in at {}".format(time.time()))
    # 遇到 await, 当前程序(print_sum)挂起, 等待compute 返回
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


def test_async_await():
    loop = asyncio.get_event_loop()
    print("start...{}".format(time.time()))
    loop.run_until_complete(print_sum(1, 2))
    print("end ...{}".format(time.time()))
    loop.close()


def main():
    # 测试 等待异步任务执行结束
    # test_run_until_complete()

    # 测试 循环 计划任务执行
    # test_call_later()

    # 测试 await
    test_async_await()


if __name__ == '__main__':
    main()
