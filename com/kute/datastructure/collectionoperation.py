#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: collectionoperation.py
@ __mtime__: 2017/3/17 14:59

常用 集合处理

"""

import string
import itertools
from pprint import pprint
from functools import lru_cache


class CollectionOperation(object):

    def __init__(self):
        pass

    def fold_to_equal_list(self, datalist=None, unit=3):
        """
        折叠集合：将集合中的元素按相同大小折叠，最后返回折叠后的所有的结果，例如
        [1, 2, 3, 4, 5, 6, 8]   =>   [[1, 2, 3], [4, 5, 6], [7, 8]]
        :param datalist:
        :param unit: default 3
        """
        if datalist and len(datalist) == 0:
            raise ValueError('datalist should not be empty.')
        size = len(datalist)
        unit = unit or 3
        for i in range(0, size, unit):
            yield datalist[i: i + unit]

    def subtract(self, list1, list2):
        """差集
        """
        return list(set(list1) - set(list2))

    @lru_cache(maxsize=3000, typed=False)
    def gen_suffix(self, start='a', end='z'):
        """
        :param start:
        :param end:
        """
        seedlist = [''.join(x) for x in itertools.product(string.ascii_lowercase, repeat=len(start))]
        return seedlist[seedlist.index(start): seedlist.index(end) + 1]


def main():
    datalist = [1, 2, 3, 4, 5, 6, 7, 8]
    operation = CollectionOperation()

    #
    # gen = operation.fold_to_equal_list(datalist, 3)
    # print([e for e in gen])

    # ['ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az', 'ba', 'bb', 'bc', 'bd', 'be']
    result = operation.gen_suffix('ao', 'be')
    print(result)


if __name__ == "__main__":
    main()
