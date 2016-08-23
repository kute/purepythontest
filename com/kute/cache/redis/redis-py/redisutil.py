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
import time


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

    def exists(self, key):
        return self._connection_redis().exists(name=key)

    def existsbatch(self, *keys):
        return [self.exists(key) for key in keys]

    def existsbatchbypipeline(self, *keys):
        with self.pipeline() as pipe:
            for key in keys:
                pipe.exists(key)
            return pipe.execute()

    def delete(self, *keys):
        return self._connection_redis().delete(*keys)

    def set(self, key, value):
        return self._connection_redis().set(name=key, value=value)

    def get(self, key):
        return self._connection_redis().get(name=key)

    def pipeline(self, transaction=True):
        return self._connection_redis().pipeline(transaction=transaction)

    def incr(self, key, value=1):
        self._connection_redis().incr(name=key, amount=value)

    def incrby(self, key, value):
        self._connection_redis().incrby(key, value)

    def zadd(self, key, score, member):
        self._connection_redis().zadd(key, score, member)

    def zaddbatch(self, key, paramdict):
        """
        批量添加
        : paramdict 字典类型, 如{"key": score}
        """
        if not key or not paramdict or not isinstance(paramdict, dict):
            return
        with self.pipeline() as pipe:
            for member, score in paramdict.items():
                pipe.zadd(key, score, member)
            pipe.execute(raise_on_error=True)

    def zrange(self, name, start, end, desc=False, withscores=False,
               score_cast_func=float):
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results descendingly

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value
        """
        self._connection_redis().zrange(name, start, end, desc, withscores, score_cast_func)

    def zrank(self, key, member):
        return self._connection_redis().zrank(key, member)

    def zcount(self, key, min, max):
        return self._connection_redis().zcount(key, min, max)

    def zcard(self, key):
        return self._connection_redis().zcard(key)

    def execute_command(self, *args, **options):
        self._connection_redis().execute_command(*args, **options)

    def regist_lua_script(self, lua=None):
        """
        执行lua脚本
        :lua
        """
        return self._connection_redis().register_script(lua)


def main():
    ru = RedisUtil(password="kuteredis")
    myzsetkey = "kute_zset"
    # ru.zadd(myzsetkey, time.clock(), "chinamember")
    mydict = {"china2": float(0.1), "japan2": float(0.2)}
    # ru.zaddbatch(myzsetkey, mydict)
    print(ru.existsbatch("a", "b", "kute_zset"))
    print(ru.existsbatchbypipeline("a", "b", "kute_zset"))


if __name__ == "__main__":
    main()
