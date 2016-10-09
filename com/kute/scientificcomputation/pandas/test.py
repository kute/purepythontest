#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/22 21:18'

"""

"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


def main():
    # Series 带索引的一维数组
    a = Series([1, 2, 3, 4])
    print(a[0])
    print(a[[0, 2]])

    b = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    b['a']  # 1
    b[['a', 'd']]  # 可以使用索引里的值来选择一个单一值或一个值集
    b.index
    b.values

    # 因为 Series 是带索引的,所以可以把它当做一个字典对待
    mydict = dict(a=1, b=2, c=3, d=4)
    a = Series(mydict)  # 按key排序, 字典的key被当做索引
    "a" in a
    myindex = ["a", "b", "c", "f"]
    b = Series(data=mydict, index=myindex)
    print(b)  # 因为 索引 f 没有对应的value,所以 值 是NaN
    a + b

    # dataFrame
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    column = ['year', 'state', 'pop', 'notkey']  # 指定 列 顺序
    index = ['a', 'b', 'c', 'd', 'e']  # 指定 索引,默认 0, 1, ...
    frame = DataFrame(data, columns=column, index=index)
    frame['year']
    frame['year']['c']
    frame.year
    frame.year.c
    frame.ix['c']  # 行 访问
    frame.columns
    frame['notkey'] = 3  # frame.notkey = 3
    frame.notkey = np.arange(1, 6)

    frame['new'] = np.arange(2, 7)  # 添加新 列


if __name__ == '__main__':
    main()
