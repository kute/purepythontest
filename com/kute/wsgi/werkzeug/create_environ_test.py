#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/10/10 20:47'

"""

werkzeug.test.create_environ 参数
@see EnvironBuilder

"""

from werkzeug.test import create_environ
from werkzeug.wrappers import Request
from io import StringIO


def main():
    try:

        body = "name=kute&pwd=encoded"
        querystring = "foo=bar&another=haha"

        environ_dict = dict(path='/root/bac', base_url='http://localhost:8888', query_string=querystring, method='POST',
                            content_length=len(body),
                            content_type='application/x-www-form-urlencoded',
                            input_stream=StringIO(body), errors_stream=None, multithread=False,
                            multiprocess=False, run_once=False, headers=None, data=None,
                            environ_base=None, environ_overrides=None, charset='utf-8')

        # 1
        environ = create_environ(**environ_dict)
        request = Request(environ)
        info(request)

        # 2
        newrequest = Request.from_values(**environ_dict)
        info(newrequest)

    except Exception as e:
        print(e)


def info(request):
    print(request.method, request.args['foo'], request.url, request.form, request.host, request.scheme)


if __name__ == '__main__':
    main()
