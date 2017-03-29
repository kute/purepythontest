#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: disuser.py
@ __mtime__: 2017/3/29 11:45

检索 重复 邮箱用户

原始数据量在 一亿

"""

import pandas as pd
from pandas import Series


def main():
    try:
        path = "/home/longbai/commentdata/UserInfo.txt"
        usercolumns = ['userid', 'useremail', 'anonymous', 'avatar']
        userdfreader = pd.read_csv(path, header=None, sep='#V_V#A_A#', iterator=True, encoding='utf-8', names=usercolumns, engine='python')
        # userdf = pd.read_csv(path, header=None, sep='#V_V#A_A#', encoding='utf-8', names=usercolumns, engine='python')
        goon = True
        c = Series()
        total = 0
        while goon:
            try:
                infochunk = userdfreader.get_chunk(1000000)
                total += 1
                if not infochunk.empty:
                    emailseries = infochunk['useremail'].value_counts()
                    repeatemail = emailseries[emailseries > 1]
                    if not repeatemail.empty():
                        c = c + repeatemail
                print('repeat email length is {}, total={}'.format(len(c), total))
            except StopIteration:
                print('..........over............')
                goon = False
        print('.....save file start.........')
        c.to_csv('useremail.csv', encoding='utf-8', mode='a')
        print('.....save file over.........')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
