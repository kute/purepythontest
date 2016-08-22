#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: simpletest.py
@ __mtime__: 2016/8/22 12:04

"""

import redis
from kute.easylog.easylog import geteasylog


easylog = geteasylog()


class RedisUtil(object):
    def __init__(self, host="127.0.0.1", port=639, db=0, passport=None, pool=None):
        self.host = host
        self.port = port
        self.db = db
        self.passport = passport
        self.pool = pool

    def _connection_redis(self):
        r = redis.StrictRedis(
            host=self.host,
            port=self.port,
            db=self.db,
            password=self.passport,
            connection_pool=self.pool
        )
        return r

    def keys(self, pattern="*"):
        return self._connection_redis().keys(pattern=pattern)


def main():
    ru = RedisUtil(host="localhost", passport="kuteredis")
    easylog.info(ru.keys())


if __name__ == "__main__":
    main()
