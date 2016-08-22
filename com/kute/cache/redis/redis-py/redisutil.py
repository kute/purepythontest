#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: redisutil.py
@ __mtime__: 2016/8/22 12:04

"""

import redis
from kute.easylog.easylog import geteasylog


easylog = geteasylog()


class RedisUtil(object):
    """
        redis connection util

    """
    def __init__(self, host="127.0.0.1", port=6379, db=0, password=None, pool=None):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        if not pool:
            self.pool = self._create_connection_pool()
        else:
            self.pool = pool

    def _create_connection_pool(self, max_connections=1000):
        return redis.ConnectionPool(
            host=self.host,
            port=self.port,
            db=self.db,
            password=self.password,
            max_connections=max_connections
        )

    def _connection_redis(self):
        r = redis.StrictRedis(connection_pool=self.pool)
        return r

    def keys(self, pattern="*"):
        return self._connection_redis().keys(pattern=pattern)

    def set(self, name, value):
        return self._connection_redis().set(name=name, value=value)

    def get(self, name):
        return self._connection_redis().get(name=name)

    def pipeline(self, transaction=True):
        return self._connection_redis().pipeline(transaction=transaction)

    def regist_lua_script(self, lua=None):
        """
        执行lua脚本
        :lua
        """
        return self._connection_redis().register_script(lua)


def main():
    ru = RedisUtil(host="localhost", password="kuteredis")
    easylog.info(ru.keys())


if __name__ == "__main__":
    main()
