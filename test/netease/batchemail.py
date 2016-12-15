#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: batchemail.py
@ __mtime__: 2016/11/9 17:45

"""
import requests
from gevent.pool import Pool
from gevent import monkey
import time
import json
import base64

monkey.patch_all()


url = "http://comment.news.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/users/{}?time={}"


def dopost(userid):
    try:
        response = requests.get(url.format(userid, time.time()))
        if response:
            resobj = json.loads(response.text, encoding="utf-8")
            # print(resobj)
            if resobj and "code" not in resobj and "username" in resobj:
                encodeemail = resobj["username"]
                email = base64.decodebytes(bytes(encodeemail, "utf-8"))
                if email:
                    with open("follower.txt", "a") as f:
                        f.write("{} {}".format(userid, email.decode("utf-8")) + "\n")
                        print("deal with:{}={}".format(userid, email.decode("utf-8")))
    except Exception as e:
        print(e, userid)


def main():
    filename = "b.txt"
    with open(filename) as f:
        pool = Pool(20)
        plist = []
        for passport in f:
            # print(passport.strip())
            plist.append(passport.strip())
            # if len(plist) >= 100:
        pool.map(dopost, plist)
        # plist.clear()


if __name__ == "__main__":
    main()
