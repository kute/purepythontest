#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/1/28 19:04'

"""

http://pandas.pydata.org/pandas-docs/stable/text.html

"""

import pandas as pd
from pandas import Series
import numpy as np


def main():
    n = np.random.randint(9, 20)

    s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
    s.str.lower()  # NaN 不会改变
    s.str.len()  # 字符长度
    s.str.strip()

    # Series 带索引的一维数组
    a = Series([1, 2, 3, 4])
    a[0]  # 默认索引 从 0 开始
    a[[0, 2]]  # 多个索引访问

    b = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    b['a']  # 索引访问
    b[['a', 'd']]  # 可以使用索引里的值来选择一个单一值或一个值集
    b.index
    b.values

    # 因为 Series 是带索引的,所以可以把它当做一个字典对待
    mydict = dict(a=1, b=2, c=3, d=4)
    a = Series(mydict)  # 按key排序, 字典的key被当做索引
    "a" in a
    myindex = ["a", "b", "c", "f"]
    b = Series(data=mydict, index=myindex)
    # b = Series(data=mydict, index=pd.Index(myindex, copy=True))
    # 因为 索引 f 没有对应的value,所以 值 是NaN
    a + b

    s2 = pd.Series(['a_b_c', 'c_d_e', np.nan, 'f_g_h'])
    result = s2.str.split("_")  # value 分隔

    result.str.get(1)  # 访问第二个元素
    result.str[1]  # 访问第二个元素

    result = s2.str.split("_", expand=True)     # 使用 expand 返回 dataFrame 对象
    result = s2.str.split("_", expand=True, n=1)     # 限制 split 个数

    print(result)


if __name__ == '__main__':
    main()
