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
    frame['year']['c']  # mutil-index
    frame.loc['c', 'notkey'] = 'newvalue'  # 设置值  loc(rowkey, columnkey)
    frame.iloc[2, 3] = 'newv'
    frame.loc['b':'d']
    frame[frame['notkey'].notnull()]
    frame.loc[frame.notkey.notnull()]
    frame.iloc[0:3, :]
    frame.year
    frame.year.c
    frame.ix['c']  # 行 访问, 推荐使用 loc


    # 删除 列
    del frame['year']
    result = frame.drop(['year', 'pop'], axis=1, errors='ignore')  # axis: 0: rows，1：column; error：删除不存在的列是否抛出异常

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

    # na_values：表明哪些值需要被视为 NAN
    df = pd.read_csv('2012.csv', na_values=[''])
    # 过滤 ：http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.filter.html
    df1 = df.filter(items=[col for col in df.columns if col not in ['aa', 'ff']])  # 过滤某些列
    # print(df1)
    print(df1[['Date', 'cc', 'dd']])  # 选取多个列
    print(df1.query('Date == ["02/01/2012", "01/11/2012"]'))  # 选取Date（注意值类型）值为  02/01/2012  和 01/11/2012
    df1[df1.cc.isin([0, 2])]
    print(df1.groupby('cc').filter(lambda x: len(x) > 1)['cc'].value_counts())  # 过滤  cc 列出现次数 <= 1的数据
    # vc = df1['cc'].value_counts()
    # print(vc[vc > 1])  # 过滤  cc 列出现次数 <= 1的数据
    # print(df1['cc'].value_counts())  # word count

    dates = pd.date_range('1/1/2000', periods=8)  # 生成日期

if __name__ == '__main__':
    main()

