#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/17 22:42'

"""

1. 在demo目录下执行: celery worker -A tasks -l info
2. 然后新打开一个terminal 执行 python client.py

"""

import celery
import time
print(dir(celery.registry))

from tasks import add


def main():
    print('main begin')
    result = add.delay(4, 9)
    while not result.ready():
        time.sleep(1)
        print("working .....")
    print(result.get(timeout=1))
    print('main end')


if __name__ == '__main__':
    main()
