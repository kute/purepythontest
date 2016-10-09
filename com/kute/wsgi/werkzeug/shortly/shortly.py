#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/10/8 22:03'

"""

"""

import os
import redis
from furl import furl
from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.routing import Map, Rule
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader


class Shortly(object):

    def __init__(self, redis_config):
        #: redis 配置
        self.redis = redis.StrictRedis(connection_pool=Shortly._create_connection_pool(redisconfig=redis_config))
        #: 模版配置
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(searchpath=template_path), auto_reload=True,
                                     autoescape=True)
        #: 路由
        self.url_map = self._create_route()

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
        adapter = self.url_map.bind_to_environ(environ=request.environ, server_name=None, subdomain=None)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def _create_route(self):
        return Map(rules=[
            Rule('/', endpoint='new_url'),
            Rule('/<short_id>', endpoint='follow_short_link'),
            Rule('/<short_id>+', endpoint='short_link_details')
        ], default_subdomain='')

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def on_new_url(self, request):
        error = None
        url = ''
        if request.method == 'POST':
            url = request.form['url']
            if not Shortly.is_valid_url(url):
                error = 'Please enter a valid URL'
            else:
                short_id = self.insert_url(url)
                return redirect('/%s+' % short_id)
        return self.render_template('new_url.html', error=error, url=url)

    def on_follow_short_link(self, request, short_id):
        link_target = self.redis.get('url-target:' + short_id)
        if link_target is None:
            raise NotFound()
        self.redis.incr('click-count:' + short_id)
        return redirect(link_target)

    def on_short_link_details(self, request, short_id):
        link_target = self.redis.get('url-target:' + short_id)
        if link_target is None:
            raise NotFound()
        click_count = int(self.redis.get('click-count:' + short_id) or 0)
        return self.render_template('short_link_details.html', link_target=link_target,
                                    short_id=short_id, click_count=click_count)

    @staticmethod
    def is_valid_url(url):
        f = furl(url)
        return f.scheme in ('http', 'https')

    def insert_url(self, url):
        short_id = self.redis.get('reverse-url:' + url)
        if short_id is not None:
            # 二进制转码
            return short_id.decode("utf-8")
        url_num = self.redis.incr('last-url-id')
        short_id = Shortly.base36_encode(url_num)
        self.redis.set('url-target:' + short_id, url)
        self.redis.set('reverse-url:' + url, short_id)
        return short_id

    @staticmethod
    def base36_encode(number):
        assert number >= 0, 'positive integer required'
        if number == 0:
            return '0'
        base36 = []
        while number != 0:
            number, i = divmod(number, 36)
            base36.append('0123456789abcdefghijklmnopqrstuvwxyz'[i])
        return ''.join(reversed(base36))

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
    run_simple(hostname="localhost", port=8888, application=app, use_debugger=True, use_reloader=True)


if __name__ == '__main__':
    main()
