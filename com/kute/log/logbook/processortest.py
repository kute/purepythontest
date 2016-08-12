#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: processortest.py
@ __mtime__: 2016/8/12 18:38

"""

import os
import sys
from logbook import Processor, StreamHandler, DEBUG, Logger

my_handler = StreamHandler(sys.stdout, level=DEBUG)


def inject_cwd(record):
    print(record.extra['cwd'])
    record.extra['cwd'] = os.getcwd()
    print(record.extra['cwd'])


if __name__ == "__main__":
    with my_handler.applicationbound():
        with Processor(inject_cwd).applicationbound():
            mylog = Logger("processor")
            mylog.notice("notice msg.")
            # mylog.notice("info msg.")
