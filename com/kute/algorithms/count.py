#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/6/15 11:22'

from collections import defaultdict


def main():
    ips = (
        (1, '10.121.1.1:4730'),
        (2, '127.0.0.1:4730'),
        (3, '127.0.0.1:4730')
    )

    dic = {}
    for v, k in ips:
        dic.setdefault(k, []).append((v, k))

    print dic

    result = defaultdict(list)
    for v, k in ips:
        result[k].append((v, k))
    print result


if __name__ == '__main__':
    main()
