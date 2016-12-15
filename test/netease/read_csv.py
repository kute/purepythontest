#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: read_csv.py
@ __mtime__: 2016/11/15 12:40

"""

import pandas as pd
import time
from gevent.pool import Pool
from gevent import monkey

monkey.patch_all()


# gentiefile = r"a.csv"
gentiefile = r"E:\跟贴\迁移\需求\ssn_del_2016_2nd\del20161008\gentie\userslist.txt"
# chunk = 2
chunk = 100000


def inter(df):
    loop = True
    gentiereader = pd.read_csv(gentiefile, iterator=True, header=None)
    while loop:
        try:
            gentiedf = gentiereader.get_chunk(chunk)
            result = pd.merge(gentiedf, df, how="inner", on=0)
            if not result.empty:
                result.to_csv("result.csv", mode="a", header=None, index=False)
        except StopIteration:
            loop = False
            print("gentie file stop")
        except Exception as e:
            print("gentie file exception :{}".format(e))


def main():

    # emailtypelist = ["yeah", "126", "163"]
    # for emailtype in emailtypelist:
    #     # file = r"b.csv"
    #     file = r"E:\跟贴\迁移\需求\ssn_del_2016_2nd\del20161008\{}_del20161008.txt".format(emailtype)
    #     reader = pd.read_csv(file, iterator=True, header=None)
    #     loop = True
    #     pool = Pool(4)
    #     tasklist = []
    #     while loop:
    #         try:
    #             df = reader.get_chunk(chunk)
    #             if not df.empty:
    #                 tasklist.append(df)
    #             if len(tasklist) >= 4:
    #                 pool.map(inter, tasklist)
    #                 tasklist.clear()
    #         except StopIteration:
    #             loop = False
    #             print("file stop over")
    #         except Exception as e:
    #             print("exception:{}".format(e))
    #     if len(tasklist) > 0:
    #         pool.map(inter, tasklist)
    #         tasklist.clear()

    dfa = pd.read_csv("a.csv", header=None)
    dfb = pd.read_csv("b.csv", header=None, sep="\s+", engine="python")
    print(pd.DataFrame(pd.DataFrame(dfb[1]).to_dict(), columns=["0"]).merge(dfa, on=0))
    # dfc = pd.merge(dfa, dfb[1])
    # dfc = dfa.merge(dfb, how="inner", on=0)
    # dfc = pd.merge(dfa, dfb, how="inner", on=0)
    # print(dfc)


if __name__ == "__main__":
    main()
