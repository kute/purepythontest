#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: testpandas.py
@ __mtime__: 2016/9/30 14:22

在b文件中填充 和a文件 第一列相同 cell的第二列值

"""

import pandas as pd


def main():
    try:
        afile = "E:\\logs\\a.xlsx"
        bfile = "E:\\logs\\b.xlsx"
        dfa = pd.read_excel(afile, 0, header=None)
        dfb = pd.read_excel(bfile, 0, header=None)
        dfc = pd.merge(dfa, dfb, how="inner", on=0)
        dfd = pd.merge(dfb, dfc, how="outer", on=0)
        dfd.to_excel(bfile, header=False, index=False)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
