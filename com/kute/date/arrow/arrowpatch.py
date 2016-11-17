#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/11/16 21:38'

"""

"""
import attr
import arrow

from arrow.arrow import tzinfo
import time


def main():
    now = arrow.now()
    print(now)
    print(now.datetime, type(now.datetime))
    print(now.timestamp)
    print(now.naive)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)
    print(now.date())
    print(now.time())
    print(now.format("YYYY-MM-DD HH:mm:ss"))
    print(now.replace(hour=12, minute=30))
    print(now.replace(hours=-1))  # set day=1
    print(now.replace(year=+1))  # set year=0001
    print(now.to("local"))
    print(now.humanize())
    print()

    longtime = time.time()
    print(arrow.get(longtime))
    print()

    print(arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss'))
    print(arrow.get(2013, 5, 5, 0))
    print(arrow.Arrow(2016, 10, 10, 10, 10, 10, 10))
    print()

    print(arrow.now().span("hour"))  # 1h之内的时间区间
    print()


if __name__ == '__main__':
    main()
