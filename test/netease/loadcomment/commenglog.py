#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/24 16:15'

"""

url pdocid docid userid ptime postid ip source firstLevelPostId parentPostId buildLevel channelId userProfile commentPath content vote against

"""

import pandas as pd
import os
import numpy as np


basepath = "/home/longbai/commentdata"
userinfopath = os.path.join(basepath, 'UserInfo.txt')
usertitlepath = os.path.join(basepath, 'UserTitle.txt')
vipinfopath = os.path.join(basepath, 'AppVipUser.txt')
authinfopath = os.path.join(basepath, 'UserAuthV.txt')
commentinfopath = os.path.join(basepath, 'CommentInfo2013.txt')
commentspath = os.path.join(basepath, 'Comments2013.txt')

usercolumns = ['userid', 'useremail', 'anonymous', 'avatar']
commentscolumns = ['commentId', 'threadId', 'userId', 'postId', 'rootId', 'parentId', 'createTime', 'buildLevel', 'path', 'vote', 'against', 'content']
commentinfocolums = ['commentId', 'threadId', 'ip', 'source']

chunksize = 1000000


def test():
    commentscolumns = ['commentId', 'threadId', 'userId', 'postId', 'rootId', 'parentId', 'createTime', 'buildLevel', 'path', 'vote', 'against', 'content']
    commentsdf = pd.read_csv('comments', header=None, sep='#V_V#', encoding='utf-8', names=commentscolumns, engine='python')
    # print(commentsdf[:1])
    commentinfocolums = ['commentId', 'threadId', 'ip', 'source']
    commentinfodf = pd.read_csv('commentinfo', header=None, sep='#V_V#', names=commentinfocolums, engine='python')
    # print(commentinfodf)
    mergeresult = pd.merge(commentsdf, commentinfodf, on='commentId')
    # del mergeresult['threadId_y']
    # mergeresult.rename(columns={'threadId_x': 'threadId'}, inplace=True)
    a = mergeresult.drop(['threadId_x', 'threadId_y'], axis=1)
    print(a.columns)


def main():
    try:
        userdfreader = pd.read_csv(userinfopath, header=None, sep='#V_V#A_A#', iterator=True, encoding='utf-8',
                                   names=usercolumns, engine='python')
        goon = True
        while goon:
            try:
                infochunk = userdfreader.get_chunk(chunksize)
                if not infochunk.empty:
                    pass
            except StopIteration:
                print('..........over {}............'.format(userinfopath))
                goon = False

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
