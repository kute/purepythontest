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

monkey.patch_all()


url = "http://10.164.96.127:8282/api/v1/products/a2869674571f77b5a0867c3d71db5856/" \
      "follow/user/{}/action/{}/followmove".format("urstestqy2@163.com", "follow")


def dopost(passport):
    body = dict(
        followerEmailList=passport
    )
    try:
        response = requests.post(url=url, data=body)
        print(response.text, passport)
    except Exception as e:
        print(e, passport)


def main():
    filename = "userpassport.txt"
    with open(filename) as f:
        pool = Pool(20)
        plist = []
        for passport in f:
            plist.append(passport.strip())
            if len(plist) >= 100:
                # pool.map(dopost, plist)
                plist.clear()


if __name__ == "__main__":
    main()
