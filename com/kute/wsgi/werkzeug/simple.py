#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/10/8 21:11'

"""

"""

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple


@Request.application
def application(request):
    return Response("Hello world")


if __name__ == '__main__':
    run_simple('localhost', 8888, application=application)
