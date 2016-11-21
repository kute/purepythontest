#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/11/19 12:05'

"""

"""

from logbook import Logger, FileHandler, INFO, Processor
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
del163file = "/Users/kute/work/docs/netease/data/del20161008/163_del20161008{}"

chunksize = 1000000

resultfilestr = "result-{}.txt"
validfilestr = "valid.txt"
illegalfilestr = "illegal.txt"
akey = "akey"


def filteremail():
    for sub in delary:
        delvaliddflist = []
        deluserlessdflist = []
        if sub != '163':
            deldf = pd.read_csv(delfile.format(sub), header=None, sep=",")
            for resultsub in userinfoary:
                resultdf = pd.read_csv(resultfilestr.format(resultsub), header=None, sep=",")
                validdf = pd.merge(pd.DataFrame({akey: deldf[0]}), pd.DataFrame({akey: resultdf[1]}), on=akey,
                                   how="inner")
                if not validdf.empty:
                    print("over useremail:{}".format(resultfilestr.format(resultsub)))
                    delvaliddflist.append(validdf)  # should be keep
                # TODO deleted
        else:
            for del163sub in del163ary:
                del163df = pd.read_csv(del163file.format(del163sub), header=None, sep=",")
                for resultsub2 in userinfoary:
                    resultdf2 = pd.read_csv(resultfilestr.format(resultsub2), header=None, sep=",")
                    validdf2 = pd.merge(pd.DataFrame({akey: del163df[0]}), pd.DataFrame({akey: resultdf2[1]}),
                                        on=akey, how="inner")
                    if not validdf2.empty:
                        print("over useremail:{}".format(resultfilestr.format(resultsub2)))
                        delvaliddflist.append(validdf2)  # should be keep
                    # TODO deleted
        print("over delsub:{}".format(sub))
        if len(delvaliddflist) > 0:
            pd.concat(delvaliddflist).to_csv(validfilestr, index=False, mode="a")
        if len(deluserlessdflist) > 0:
            pd.concat(deluserlessdflist).to_csv(illegalfilestr, index=False, mode="a")
        delvaliddflist.clear()
        deluserlessdflist.clear()


def filteruserid():
    usercommentdf = pd.read_csv(usercommentfile, header=None, sep="\s+")
    # reader = pd.read_csv(usercommentfile.format("ad"), iterator=True, header=None, sep="\s+")
    for infosub in userinfoary:
        resultlist = []
        inforeader = pd.read_csv(userinfofile.format(infosub), iterator=True, header=None,
                                 sep="	|	",
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
        pd.concat(resultlist).to_csv(resultfilestr.format(infosub), index=False, mode="w")


def main():
    # filteruserid()
    filteremail()


if __name__ == '__main__':
    main()
