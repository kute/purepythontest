#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/1/8 16:51'

"""
异步io
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


urls = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/',
        'http://forwhy.cf']


def get_code(url):
    return requests.get(url).status_code


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        # future-dict
        futures_urls = {executor.submit(get_code, url): url for url in urls}
        for future in as_completed(futures_urls):
            url = futures_urls[future]
            try:
                result = future.result()
            except Exception as e:
                print("exception occur:{},{}".format(url, e))
            else:
                print("{} finished {}".format(url, result))

if __name__ == '__main__':
    main()
