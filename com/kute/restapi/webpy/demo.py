#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: demo.py
@ __mtime__: 2016/8/27 16:55

"""

import web


urls = (
    '/', 'index'
)


class index:
    def GET(self):
        return "Hello, world!"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


