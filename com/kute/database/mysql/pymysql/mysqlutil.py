#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: mysqlutil.py
@ __mtime__: 2016/8/30 10:15


cursor.callproc   执行存储过程

"""

import pymysql.cursors
from kute.easylog.easylog import geteasylog


easylog = geteasylog()


class MysqlUtil(object):
    """connector util for mysql"""
    def __init__(self, host="127.0.0.1", port=3306, user="root", password="root", database="test", charset="utf-8"):
        self.host = host or "127.0.0.1"
        self.port = port or 3306
        self.user = user or "root"
        self.password = password or "root"
        self.database = database or "test"
        self.charset = charset or "utf-8"

    def _get_connection(self):
        return pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                               database=self.database)

    def insert(self, sql, *args):
        """
        :param sql: sql语句
        :param args tuple
        """
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, *args)
                connection.commit()
        finally:
            connection.close()

    def insertbatch(self, sql, argslist):
        """
        :param sql: sql语句
        :param argslist 参数集合
        """
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.executemany(sql, argslist)
                connection.commit()
        finally:
            connection.close()

    def select_one(self, sql, *args):
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, *args)
                result = cursor.fetchone()
                return result
        finally:
            connection.close()

    def select_all(self, sql, argslist, size=-1):
        """
        :param sql: 执行sql
        :param argslist: 参数列表
        :param size: 返回的结果集个数，如果为-1则全部返回
        """
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, argslist)
                if size != -1:
                    result = cursor.fetchmany(size)
                else:
                    result = cursor.fetchall()
                return result
        finally:
            connection.close()

    def transaction_sql(self, sql, tuplelist):
        """
        事务操作
        :param sql: sql
        :param tuplelist:
        """
        connection = self._get_connection()
        connection.begin()
        try:
            with connection.cursor() as cursor:
                for args in tuplelist:
                    cursor.execute(sql, args)
                    # print(args)
            connection.commit()
        except Exception as e:
            connection.rollback()
            easylog.error("error, rollback", e.args)
        finally:
            connection.close()


def main():
    pass
    # util = MysqlUtil()
    # 1. insert one
    # sql = "insert into teacher(`id`, `name`, `lastupapptime`, `topicid`) values(%s, %s, %s, %s)"
    # util.insert(sql, ('2', "kute2", '2016-08-30 17:21:56', '1400'))

    # 2. batch insert
    # sql = "insert into teacher(`id`, `name`, `lastupapptime`, `topicid`) values(%s, %s, %s, %s)"
    # argslist = [(str(i), "kute" + str(i), "2016-08-30 17:21:3" + str(i), "1299" + str(i)) for i in range(3, 9)]
    # util.insertbatch(sql, argslist)

    # 3. select one
    # sql = "select * from teacher where id = %s"
    # result = util.select_one(sql, ("1", "2"))
    # print(result)  # tuple

    # sql = "select count(1) from teacher where id < %s"
    # result = util.select_one(sql, ("6", ))
    # print(result)

    # 4. select all
    # sql = "select * from teacher where id < %s"
    # resultall = util.select_all(sql, ("9", ), 3)
    # print(resultall)  # tuple(tuple)

    # 5. transaction example
    # sql = "insert into teacher(`id`, `name`, `lastupapptime`, `topicid`) values(%s, %s, %s, %s)"
    # argslist = [(str(i), "kute" + str(i), "2016-08-30 17:21:3" + str(i), "1299" + str(i)) for i in range(8, 10)]
    # util.transaction_sql(sql, argslist)


if __name__ == "__main__":
    main()
    # print(datetime.datetime.now().__str__())
