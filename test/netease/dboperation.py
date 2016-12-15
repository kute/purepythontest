#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: dboperation.py
@ __mtime__: 2016/12/13 13:55

"""

from com.kute.database.mysql.pymysql.mysqlutil import MysqlUtil
from gevent.pool import Pool
from gevent import monkey
import logging

monkey.patch_all()

mylog = logging.getLogger(__name__)
filehandler = logging.FileHandler("data.log", encoding="utf-8")
myformat = logging.Formatter('%(message)s')
filehandler.setFormatter(myformat)
mylog.addHandler(filehandler)

conn = MysqlUtil("localhost", 4413, "comment_read", "comment_read", "comment-mirror")


def loguseridentify(userid):
    if not userid:
        return
    vcount = conn.select_one("select count(1) from UserAuthV where userid = %s", (userid, ))
    vipinfo = conn.select_one("select vipInfo from AppVipUser where userid = %s", (userid, ))
    loglist = list([userid])
    loglist.append(vcount[0] if vcount else 0)
    loglist.append(1 if vipinfo and len(vipinfo) > 0 and vipinfo[0] else 0)
    mylog.info(",".join(str(i) for i in loglist))


def main():
    # with open("userid.txt") as f:
    #     plist = []
    #     pool = Pool(20)
    #     for userid in f:
    #         userid = userid.strip()
    #         plist.append(userid)
    #         if len(plist) > 100:
    #             pool.map(loguseridentify, plist)
    #             plist.clear()
    #     if len(plist) > 0:
    #             pool.map(loguseridentify, plist)

    loguseridentify(10086251)
    # mylog.info("tt")

if __name__ == "__main__":
    main()
