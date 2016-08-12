#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/9 22:20'

"""

SyslogHandler 不支持在windows平台使用，见：https://github.com/getlogbook/logbook/issues/186

push_application 将handler压入application stack中
applicationbound 同理，结合with使用

"""

from logbook import Logger, StreamHandler, SyslogHandler, ERROR, INFO
import sys


StreamHandler(sys.stdout, level=INFO).push_application()


def test1():
    log = Logger('Logbook-test-1')
    log.critical("critical")
    log.error("error")
    log.warn("warn")
    log.notice("notice")
    log.info("test")
    log.debug("debug")


def test2():
    log = Logger('Logbook-test-2')
    log.critical("critical")
    log.error("error")
    log.warn("warn")
    log.notice("notice")
    log.info("test")
    log.debug("debug")


if __name__ == '__main__':
    test1()
    with StreamHandler(sys.stderr, level=ERROR).applicationbound():
        test2()

