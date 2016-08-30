#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/7/19 21:03'

import requests
from contextlib import closing
from com.kute.http.example.getcookiefrom163 import GetCookieFrom163Util


def main():
    url = "http://comment.news.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/" \
          "threads/BSA22QBA00014AED/comments"

    body = dict(
        board="news_bbs",
        content="人微言轻的,没办法啊3"
    )

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0"
    }

    util = GetCookieFrom163Util("xxxxxxx", "xxxxxxxx")

    cookies = {
        "NTES_SESS": util.cookie
    }

    # 每次响应生成后调用
    hooks = dict(
        response=printInfo
    )

    try:
        with closing(requests.post(
            url=url,
            data=body,
            headers=headers,
            cookies=cookies,
            stream=True,  # 延迟下载response,直到访问res.content时才下载
            timeout=1000,
            hooks=hooks
        )) as res:
            print("over")
    except Exception as e:
        print( e.message)


def printInfo(res, *args, **kwargs):
    print(res.url)
    print( res.status_code)
    print (res.text)
    print (res.content)
    print (res.headers)
    print (res.cookies)
    print (res.request.headers)


if __name__ == '__main__':
    main()
