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
        pool = Pool(20)
        print("======begin filename:{}=====".format(filename))
        emailary = pd.read_csv(os.path.join(basepath, 'data/{}'.format(filename)), sep="\n", header=None)
        sumlist = slicesublist(list(emailary[0]))
        size = len(sumlist)
        total = 0
        for i in range(0, size, 20):
            subdata = sumlist[i: i + 20]
            total += len(subdata)
            pool.map(select_userid, subdata)
        print("======filename:{} finished end {}".format(filename, total))
        sleep(15)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
