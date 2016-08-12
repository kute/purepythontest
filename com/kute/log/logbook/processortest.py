#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: processortest.py
@ __mtime__: 2016/8/12 18:38

日志处理器

"""

import os
import sys
from logbook import Processor, StreamHandler, DEBUG, Logger, FileHandler

my_handler = FileHandler("test.log", encoding="utf-8", level=DEBUG)
# my_handler = StreamHandler(sys.stdout, level=DEBUG)


def log_other_info(record):
    """
    """
    record.extra['myname'] = 'kute'
    record.extra['mycwd'] = os.getcwd()


if __name__ == "__main__":
    with my_handler.applicationbound():
        with Processor(log_other_info).applicationbound():
            mylog = Logger("processor")
            mylog.notice("notice msg.")
            # mylog.notice("info msg.")
