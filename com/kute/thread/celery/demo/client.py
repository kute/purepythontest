#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/17 22:42'

"""

"""

import celery
print(dir(celery.registry))

from demo import add


def main():
    print('main begin')
    result = add.delay(4, 9)
    while not result.ready():
        print("working .....")
    print(result.get(timeout=1))
    print('main end')


if __name__ == '__main__':
    main()
