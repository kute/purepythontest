#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/8/20 14:36'

"""

"""

from com.kute.thread.asyncio.event_loop import EventorLoop
import time


def example_1():
    def work(e1, n):
        n = n or 10
        for i in range(1, n + 1):
            print("work output value:{}".format(i))
            time.sleep(1)
        e1.stop()

    e = EventorLoop()
    e.call_soon(callback=work, n=8)


def example_2():
    def print_current_date(e1, endtime):
        print("current date is {}".format(time.ctime()))
        if e1.time() < endtime:
            e1.call_later(1, callback=print_current_date, endtime=endtime)
        else:
            e1.stop()

    e = EventorLoop()
    etime = e.time() + 8
    e.call_soon(callback=print_current_date, endtime=etime)
    # e.call_later(5, callback=print_current_date, endtime=etime)


def example_3():
    async def work(n):
        n = n or 10
        total = 0
        for i in range(1, n + 1):
            total += i
            print("work output value:{}".format(i))
            time.sleep(1)
        return total

    e = EventorLoop()
    result = e.run_until_complete(work(n=8))
    print("total value is {}".format(result))


def main():
    # example_1()
    example_2()
    # example_3()
    print("done")


if __name__ == '__main__':
    main()
