#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: followrequtest.py
@ __mtime__: 2016/8/30 13:05

"""

import requests
from gevent.pool import Pool
from gevent import monkey
import json
from logbook import Logger, FileHandler, INFO, Processor

monkey.patch_all()

formatstr = "{record.time}:{record.message}"
handler = FileHandler(filename="test.log", mode="a", encoding="utf-8", level=INFO, format_string=formatstr)\
    .push_application()
mylog = Logger("processor")


url = "http://10.164.96.127:8282/api/v1/products/a2869674571f77b5a0867c3d71db5856/" \
      "follow/user/{}/action/{}/followmove".format("urstestqy2@163.com", "follow")


threadurl = "http://comment.news.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/{}"

userextpurl = "http://223.252.207.32/extapi/v1/app/products/aac69c917e1787ad7bd86cd86afe6efc/users/{}/exp"


def dopost(passport):
    body = dict(
        followerEmailList=passport
    )
    try:
        response = requests.post(url=url, data=body)
        print(response.text, passport)
    except Exception as e:
        print(e, passport)


def doget(docId):
    try:
        response = requests.get(threadurl.format(docId))
        if response and response.status_code == 200:
            threadobj = json.loads(response.text)
            if threadobj and "tcount" in threadobj:
                tcount = threadobj["tcount"]
                if tcount > 0:
                    mylog.info("{},{}".format(docId, tcount))
    except Exception as e:
        print(e)


def dogetuserext(passport):
    try:
        requests.get(userextpurl.format(passport))
    except Exception as e:
        print(e)


def main():
    filename = "flow_user_ip.txt"
    total = 0
    with open(filename) as f:
        pool = Pool(20)
        plist = []
        for passport in f:
            plist.append(passport.strip())
            if len(plist) >= 100:
                total += 100
                print("deal {}".format(total))
                pool.map(dogetuserext, plist)
                plist.clear()
        if len(plist) > 0:
            total += len(plist)
            pool.map(dogetuserext, plist)
            plist.clear()
        print("total num:{}".format(total))


if __name__ == "__main__":
    main()
