#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: batchgetthread.py
@ __mtime__: 2016/8/27 11:26

测试 批量读取文章信息（nginx + python + redis）

"""

import requests
import json
import pickle
from com.kute.cache.redis.redispy.redisutil import RedisUtil

url = "http://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/{}"


class ThreadStatus(object):
    """thread status"""
    def __init__(self, app="on", web="on", audio="on", against="on", joincount="on", label="on"):
        self.app = app
        self.web = web
        self.audio = audio
        self.against = against
        self.joincount = joincount
        self.label = label


class CommentThread(object):
    """
    thread info class
    """
    def __init__(self, docid, url, title, boardid, createtime, modifytime, isaudit, vote, against, tcount,
                 rcount, cmtvote, cmtagainst, status=ThreadStatus()):
        self.docid = docid
        self.url = url
        self.title = title
        self.boardid = boardid
        self.createtime = createtime
        self.modifytime = modifytime
        self.isaudit = isaudit
        self.vote = vote
        self.against = against
        self.tcount = tcount
        self.rcount = rcount
        self.cmtvote = cmtvote
        self.cmtagainst = cmtagainst
        self.status = status

    @staticmethod
    def _thread_object_hook(jsonobj):
        if jsonobj and "docId" in jsonobj:
            statusjson = jsonobj["status"]
            status = ThreadStatus(statusjson["app"], statusjson["web"],
                                  statusjson["audio"], statusjson["against"],
                                  statusjson["joincount"], statusjson["label"])
            return CommentThread(jsonobj["docId"], jsonobj["url"], jsonobj["title"], jsonobj["boardId"],
                                 jsonobj["createTime"], jsonobj["modifyTime"], jsonobj["isAudit"], jsonobj["vote"],
                                 jsonobj["against"], jsonobj["tcount"], jsonobj["rcount"],
                                 jsonobj["cmtVote"], jsonobj["cmtAgainst"], status)
        return jsonobj

    @staticmethod
    def jsonstr_to_object(threadjsonstr):
        return json.loads(s=threadjsonstr, encoding="utf-8", object_hook=CommentThread._thread_object_hook)

    @staticmethod
    def getthreadkey(docid):
        return "_".join(["thread_info", docid, "key"])


def requestthreadinfo(url):
    threadjsonstr = requests.get(url).text
    # print(threadjsonstr)
    return CommentThread.jsonstr_to_object(threadjsonstr)


def save_to_redis(docid):
    threadurl = url.format(docid)
    # print(threadurl)
    thread = requestthreadinfo(threadurl)
    # print(thread.)
    if thread:
        redisclient = RedisUtil(password="kuteredis")
        key = CommentThread.getthreadkey(docid)
        if redisclient.exists(key):
            redisclient.delete(key)
        # pickobj = pickle.dumps(thread)
        redisclient.set(key, thread)


def main():
    docid = "BVEOVUPN00031H2L"
    redisclient = RedisUtil(password="kuteredis")
    # save_to_redis(docid)
    thread = redisclient.get(CommentThread.getthreadkey(docid))
    print(type(thread))
    # print(dir(thread.decode("utf-8")))
    # print(str(thread, encoding="utf-8"))
    # print(json.dumps(thread.decode("utf-8"), default=lambda obj: obj.__dict__))


if __name__ == "__main__":
    main()
