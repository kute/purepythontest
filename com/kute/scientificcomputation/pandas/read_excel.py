#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/27 20:43'

"""
http://pandas.pydata.org/pandas-docs/stable/io.html#io-excel-reader


"""

import pandas as pd

from io import BytesIO


def read(filepath):
    data = {}
    with pd.ExcelFile(filepath) as xlsx:
        # parse_cols: 解析指定 列
        # index_col: 指定哪列作为索引
        data['mysheet'] = pd.read_excel(xlsx, sheetname="mysheet", index_col=0, parse_cols=[0, 1, 2, 3, 4, 5, 6], na_values=["null"])
        print(data)


def write(filepath):
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    bio = BytesIO()
    df1 = pd.DataFrame(data)
    with pd.ExcelWriter(filepath) as writer:
        df1.to_excel(writer, sheet_name='Sheet1')


def main():
    try:
        filepath = "/Users/kute/Documents/test.xlsx"
        read(filepath)

        write(filepath)


    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
