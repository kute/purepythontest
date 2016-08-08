#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/7/19 21:37'

import requests
from contextlib import closing
import json


def main():

    url = "http://comment.news.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/BSA22QBA00014AED/" \
        "comments/BSA22QBA00014AED_2524880785?ibc=newspc"
    hook = dict(
        response=callback_function
    )
    with closing(requests.get(url, stream=True, hooks=hook)) as res:
        print res.json()


def callback_function(res, *args, **kwargs):
    print res.url


if __name__ == '__main__':
    main()
