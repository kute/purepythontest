#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/7/19 21:26'


import requests


def main():
    try:
        requests.get("https://www.baidu.com/")
    except Exception as e:
        print( e)


if __name__ == '__main__':
    main()
