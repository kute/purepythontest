#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/10 20:29'

"""

"""

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w')


def main():
    mylog = logging.getLogger(__name__)
    mylog.setLevel(logging.DEBUG)
    consoleHandler = logging.StreamHandler()
    myformat = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    consoleHandler.setFormatter(myformat)
    mylog.addHandler(consoleHandler)
    mylog.info("tset")

if __name__ == '__main__':
    main()
