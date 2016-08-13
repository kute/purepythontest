#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: logrecord.py
@ __mtime__: 2016/8/13 14:23

日志对象的属性测试
LogRecord

"""

import sys
from kute.easylog.easylog import geteasylog
from logbook import StreamHandler, DEBUG, Processor, Logger


easylog = geteasylog()
StreamHandler(sys.stdout, level=DEBUG).push_application()


def printrecorddetail(record):
    easylog.info(record.channel)  # name of the logger
    easylog.info(record.dispatcher.name)
    easylog.info(record.exception_message)
    easylog.info(record.exception_name)
    easylog.info(record.extra)
    easylog.info(record.filename)
    easylog.info(record.level)
    easylog.info(record.level_name)
    easylog.info(record.message)
    easylog.info(record.msg)
    easylog.info(record.thread_name)
    easylog.info(record.time)

    easylog.info(record.to_dict(True))  # 纵览全部日志属性


if __name__ == "__main__":
    with Processor(printrecorddetail).applicationbound():
        mylog = Logger("log-record-app-name")
        mylog.info("log record detail")
