#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: commontest.py
@ __mtime__: 2016/11/15 10:59

"""

from com.kute.database.mysql.pymysql.mysqlutil import MysqlUtil


def main():
    client = MysqlUtil(host="localhost", port=4412, user="comments", password="comments",
                       database="general-comments-test")
    sql = "select * from Thread limit 1"
    result = client.select_one(sql)
    print(result)


if __name__ == "__main__":
    main()
