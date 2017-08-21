#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/8/20 14:36'

"""

"""

from com.kute.thread.asyncio.event_loop import EventorLoop
import time


async def work(loop, n):
    n = n or 10
    for i in range(1, n + 1):
        print("work output value:{}".format(i))
        time.sleep(1)
    loop.stop()


def main():
    e = EventorLoop()
    e.call_soon(callback=work, n=8)


if __name__ == '__main__':
    main()
