#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: test.py
@ __mtime__: 2017/8/24 14:09

https://github.com/aio-libs/async-timeout

"""

import asyncio
import async_timeout


async def take():
    print("waiting seconds")
    await asyncio.sleep(5)


async def fun(loop):
    try:
        # 未在超时时间内完成，将抛出 asyncio.TimeoutError
        async with async_timeout.timeout(3, loop=loop) as att:
            print("await take:{}".format(get_current_task(loop)))
            await take()
        print(att.expired)
    except asyncio.TimeoutError:
        print("timeout occur")


def get_current_task(loop):
    return async_timeout.current_task(loop)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fun(loop))
    loop.close()


if __name__ == "__main__":
    main()
