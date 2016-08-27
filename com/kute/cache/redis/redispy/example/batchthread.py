#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: batchthread.py
@ __mtime__: 2016/8/27 15:54

"""


import requests
import redis


def getthreadurl(docid):
    return "http://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/{}".format(docid)


def getthreadkey(docid):
    return "_".join(["thread_info", docid, "key"])


def getredisclient():
    return redis.StrictRedis(host="127.0.0.1", port=6379, db=0, password="kuteredis")


def save_to_redis_str(docid):
    threadurl = getthreadurl(docid)
    redisclient = getredisclient()
    threadstr = requests.get(threadurl).text
    key = getthreadkey(docid)
    if redisclient.exists(key):
        redisclient.delete(key)
    redisclient.set(key, threadstr)


def getthreadinfo(docid):
    redisclient = getredisclient()
    return redisclient.get(getthreadkey(docid)).decode("utf-8")


def main():
    docid = "BVEOVUPN00031H2L"
    save_to_redis_str(docid)
    print(getthreadinfo(docid))

if __name__ == "__main__":
    main()
