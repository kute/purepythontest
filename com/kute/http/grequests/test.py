#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/7/24 10:34'


"""
异步请求
"""
import grequests


def main():
    urls = [
        'http://www.heroku.com',
        'http://python-tablib.org',
        'http://httpbin.org',
        'http://python-requests.org',
        'http://fakedomain/',
        'http://kennethreitz.com'
    ]
    res = (grequests.get(url) for url in urls)
    print(grequests.map(res, exception_handler=exception_handler))


def exception_handler(request, response):
    print(request.url)
    print("request error")


if __name__ == '__main__':
    main()
