#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: distinct_userid.py
@ __mtime__: 2016/11/9 14:58

"""


def main():
    try:
        with open("followuserid.txt", "a+") as follow:
            with open("followeruserid.txt", "a+") as follower:
                followlist = []
                followerlist = []
                for i in range(1, 18):
                    with open("E:\\跟贴\\迁移\\需求\\关注\\数据\\1109\\{}.sql".format(i), "r") as f:
                        for line in f:
                            lineary = line.strip().split("	")
                            if lineary[0] not in followlist:
                                followlist.append(lineary[0])
                                follow.write(lineary[0] + "\n")
                            if lineary[1] not in followerlist:
                                followerlist.append(lineary[1])
                                follower.write(lineary[1] + "\n")
                    followlist.clear()
                    followerlist.clear()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
