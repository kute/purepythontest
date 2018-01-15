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
import functools


# define coroutine function
async def hello():
    print("hello")
    await asyncio.sleep(5)  # 模拟耗时操作
    print("hello after 5 seconds")


def test_run_until_complete():

    loop = asyncio.get_event_loop()  # <=>  loop = asyncio.get_event_loop_policy().get_event_loop()
    print("main start")
    hello_obj = hello()
    loop.run_until_complete(hello_obj)
    print(asyncio.iscoroutine(hello_obj))
    print(asyncio.iscoroutinefunction(hello))
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
    return result


def test_async_await():
    loop = asyncio.get_event_loop()  # <=> asyncio.get_event_loop_policy().get_event_loop()
    print("start...{}".format(time.time()))

    # loop.run_until_complete(print_sum(1, 2))

    # 等价于
    obj_coro = print_sum(1, 2)
    task = loop.create_task(obj_coro)
    # task = asyncio.ensure_future(obj_coro)
    # 绑定回调函数处理结果
    def callback_1(future):
        print("print sum callback return value is {}".format(future.result()))
    def callback_2(x, future):
        print("print sum callback mutil param return values is {}={}".format(x, future.result()))
    task.add_done_callback(callback_1)
    # 多参数
    task.add_done_callback(functools.partial(callback_2, "i am x"))
    loop.run_until_complete(task)
    print("end ...{}".format(time.time()))
    # 不绑定回调函数,判断状态取结果
    if task.done():
        print("result is :{}".format(task.result()))

    loop.close()


def main():
    # 测试 等待异步任务执行结束
    test_run_until_complete()

    # 测试 循环 计划任务执行
    # test_call_later()

    # 测试 await
    # test_async_await()
    print("done")


if __name__ == '__main__':
    main()
