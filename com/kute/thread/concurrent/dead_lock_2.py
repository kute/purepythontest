#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/1/8 16:36'

"""

wait for self
"""

import time
from concurrent.futures import ThreadPoolExecutor


def wait_self():
    print("self start at:{}".format(time.clock()))
    print(ps.result())
    return "self"


self = ThreadPoolExecutor(max_workers=1)
ps = self.submit(wait_self)


def main():
    pass


if __name__ == '__main__':
    main()
