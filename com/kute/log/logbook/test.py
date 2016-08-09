#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/9 22:20'

"""

"""

from logbook import Logger, StreamHandler
import sys


def main():
    StreamHandler(sys.stdout).push_application()
    log = Logger('Logbook')
    log.info("test")


if __name__ == '__main__':
    main()
