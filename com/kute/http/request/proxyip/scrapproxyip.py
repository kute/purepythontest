#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/11/17 22:25'

"""

"""

from bs4 import BeautifulSoup
import requests
import attr


@attr.s
class ProxyIp(object):
    server = attr.ib()
    live = attr.ib()
    country = attr.ib(default="china")
    ip = attr.ib(default="127.0.0.1")
    port = attr.ib(default=80, convert=int)
    anonymous = attr.ib(default=True)


class ScrapProxyTask(object):

    def gen_sites(self, file="website.txt"):
        if not file:
            raise ValueError("No file site special")
        with open(file) as f:
            for line in f:
                yield line.strip()

    def xicidaili(self, url="http://www.xicidaili.com/"):
        html = requests.get(url)
        if html.status_code == 200:
            pass


def main():
    response = requests.get("http://api.xicidaili.com/free2016.txt", timeout=2)
    print(response.text)


if __name__ == '__main__':
    main()
