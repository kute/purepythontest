#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/11/19 18:28'

"""

"""

import pandas as pd
import re
import os


def main():
    dfa = pd.read_csv("a.txt", header=None, sep="\s+")
    dfb = pd.read_csv("b.txt", header=None, sep=",", engine="python")

    # dfc = pd.merge(dfa, dfb, on=0, how="left")
    # print(dfc.index)
    # print(dfb.index)
    # a = dfa[0].values
    # b = dfb[0].values
    # c = set(a) - set(b)
    # print(list(c)[:3])
    # print(c.pop())
    # dfc.to_csv("dfc.txt", index=False)

    # usercommentfile = "/Users/kute/work/docs/netease/data/UserComment"
    # userinfoaa = "/Users/kute/work/docs/netease/data/UserInfoaa"
    # usercommentdf = pd.read_csv(usercommentfile, header=None, sep="\s+")
    # userinfodf = pd.read_csv(userinfoaa, header=None, sep="	|	", engine="python")
    # result = set(userinfodf[0]) - set(usercommentdf[0])
    # print(list(result)[:10])

    # print(dfa)
    # print(dfb)
    da = {"akey": dfa[0]}
    db = {"akey": dfb[1]}
    dfas = pd.DataFrame(data=da)
    dfbs = pd.DataFrame(data=db)
    print(dfas)
    print(dfbs)
    dfc = pd.merge(dfbs, dfas, on="akey", how="inner")
    print(dfc)


if __name__ == '__main__':
    main()
