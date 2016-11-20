#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/11/19 12:05'

"""

"""

from logbook import Logger, FileHandler, INFO, Processor
import string
import pandas as pd


formatstr = "{record.time}:{record.message}"
handler = FileHandler(filename="test.log", mode="a", encoding="utf-8", level=INFO, format_string=formatstr)\
    .push_application()
mylog = Logger("processor")

usercommentfile = "/Users/kute/work/docs/netease/data/UserComment"
usercommentary = ["aa", "ab", "ac", "ad"]

userinfofile = "/Users/kute/work/docs/netease/data/UserInfoa{}"
userinfoary = [chr(i) for i in range(ord('a'), ord('v') + 1)]

delfile = "/Users/kute/work/docs/netease/data/del20161008/{}_del20161008.txt"
delary = ["yeah", "126", "163"]
# ['aa', 'ab', ..., 'be']
del163ary = [('a' if i <= ord('z') else 'b') +
             chr(i if i <= ord('z') else i - ord('z') + ord('a') - 1) for i in range(ord('a'), ord('z') + 6)]

chunksize = 1000000


def filter():
    for sub in delary:
        pass


def main():
    usercommentdf = pd.read_csv(usercommentfile, header=None, sep="\s+")
    # reader = pd.read_csv(usercommentfile.format("ad"), iterator=True, header=None, sep="\s+")
    for infosub in userinfoary:
        resultlist = []
        inforeader = pd.read_csv(userinfofile.format(infosub), iterator=True, header=None,
                                 sep="	|	",
                                 # sep="	",
                                 engine="python",
                                 encoding="utf-8")
        goon = True
        while goon:
            try:
                infochunk = inforeader.get_chunk(chunksize)
                if not infochunk.empty:
                    result = pd.merge(usercommentdf, infochunk, how="inner", on=0)
                    if not result.empty:
                        resultlist.append(result)
            except StopIteration:
                goon = False
        print("over file:{}".format(infosub))
        pd.concat(resultlist).to_csv("result-{}.txt".format(infosub), index=False, mode="w")


if __name__ == '__main__':
    main()
