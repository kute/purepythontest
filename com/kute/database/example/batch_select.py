#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: batch_select.py
@ __mtime__: 2017/3/16 14:59

给定一批 用户通行证 批量多线程查询用户的信息并存于文件

"""
from gevent import monkey, sleep
monkey.patch_all()
import os
import pandas as pd
from gevent.pool import Pool
from eventor import Eventor
import logging
from com.kute.database.mysql.pymysql.mysqlutil import MysqlUtil


logging.basicConfig(filename='result.log', filemode='a', format='%(message)s', datefmt='%H:%M:%S', level=logging.INFO)
basepath = os.path.dirname(__file__)
# TODO
dbconfig = {
    'database': '',
    'port': 3306,
    'user': '',
    'passport': ''
}


def genfilenamelist(filenameprefix):
    sublist = [('a' if i <= ord('z') else 'b') + chr(i if i <= ord('z') else i - ord('z') + ord('a') - 1) for i in
               range(ord('a'), ord('u') + 1)]
    for sub in sublist:
        yield '{}{}'.format(filenameprefix, sub)


def select_userid(passportlist):
    sql = 'select userid, useremail from UserInfo where useremail in %s'
    # 注意数据库链接，是否要功用一个 还是 新建多个
    util = MysqlUtil(port=dbconfig['port'], user=dbconfig['user'], password=dbconfig['passport'],
                     database=dbconfig['database'])
    result = util.select_all(sql, (passportlist, ))
    if len(result) > 0:
        for user in result:
            logging.info(list(user))


def slicesublist(datalist):
    sumlist = []
    size = len(datalist)
    for i in range(0, size, 20):
        subdata = datalist[i: i + 20]
        sumlist.append(subdata)
    return sumlist


def main():
    try:
        # 第一种方式
        # pool = Pool(20)
        # for filename in genfilenamelist('appuser'):
        #     print("======begin filename:{}=====".format(filename))
        #     emailary = pd.read_csv(os.path.join(basepath, 'data/{}'.format(filename)), sep="\n", header=None)
        #     sumlist = slicesublist(list(emailary[0]))
        #     size = len(sumlist)
        #     total = 0
        #     for i in range(0, size, 20):
        #         subdata = sumlist[i: i + 20]
        #         total += len(subdata)
        #         pool.map(select_userid, subdata)
        #     print("======filename:{} finished end {}".format(filename, total))
        #     sleep(15)

        # 第二种方式
        # e = Eventor(threadcount=20, taskunitcount=20, func=select_userid, interval=1)
        # for filename in genfilenamelist('appuser'):
        #     print("======begin filename:{}=====".format(filename))
        #     emailary = pd.read_csv(os.path.join(basepath, 'data/{}'.format(filename)), sep="\n", header=None)
        #     sumlist = slicesublist(list(emailary[0]))
        #     e.run_with_tasklist(sumlist)
        #     sleep(15)
        print('suggest second.')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
