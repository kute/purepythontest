#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/10/8 22:03'

"""

"""

import os
import redis
from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import SharedDataMiddleware


class Shortly(object):

    def __init__(self, redis_config):
        self.redis = redis.StrictRedis(connection_pool=Shortly._create_connection_pool(redisconfig=redis_config))

    @staticmethod
    def _create_connection_pool(redisconfig, max_connections=1000):
        return redis.ConnectionPool(
            host=redisconfig['host'],
            port=redisconfig['port'],
            db=redisconfig['db'] if 'db' in redisconfig else 0,
            password=redisconfig['password'],
            max_connections=max_connections
        )

    def dispatch_request(self, request):
        return Response("hello, world")

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(host='localhost', port=6379, password="kuteredis", with_static=True):
    app = Shortly({
        'host': host,
        'port': port,
        'password': password
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app=app.wsgi_app, exports={
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app


def main():
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple("localhost", 8888, app, True, True)


if __name__ == '__main__':
    main()
