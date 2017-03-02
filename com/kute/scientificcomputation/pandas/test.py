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
    frame.rename(columns={'year': 'yearP', 'pop': 'popP'}, inplace=True)  # 重命名列名
    frame.rename(columns=lambda cl: cl + "P", inplace=True)  # 重命名列名
    print(frame.columns)
    frame['notkey'] = 3  # frame.notkey = 3
    frame.notkey = np.arange(1, 6)

    frame['new'] = np.arange(2, 7)  # 添加新 列

    # create dataframe
    a = {'a': 1, 'b': 2}
    b = pd.Series([1, 2, 3], index=list('abc'))
    c = pd.Series([1, 2, 3])
    d = {'cc': a, 'dd': a}
    e = {'ee': b}
    f = {'ff': b, 'fff': b}
    g = {'gg': a, 'ggg': b}
    frame = DataFrame(a, index=['A', 'B', 'C'])  # 列名为 字典key，且值 为字典value的指定索引（索引个数代表行数）的dataframe
    frame = DataFrame(b)  # 列名 从 0开始, 索引为 series的索引
    frame = DataFrame(c)  # 列明 从 0开始，索引也 从 0开始
    frame = DataFrame(d)  # 列明指定为 cc和 dd， 索引为 字典key
    frame = DataFrame(e)  # 列名 为 ee， 索引为series索引
    frame = DataFrame(f)  # 列名 为 ff和fff， 索引为series索引
    frame = DataFrame(g)



if __name__ == '__main__':
    main()
