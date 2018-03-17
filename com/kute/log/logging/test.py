#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/10 20:29'

"""

"""

import logging

# requests log setting
logging.getLogger("requests").setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w')


def main():
    mylog = logging.getLogger(__name__)
    mylog.setLevel(logging.DEBUG)

    # 控制台输出
    consoleHandler = logging.StreamHandler()
    myformat = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    consoleHandler.setFormatter(myformat)

    # 输出到文件
    filehandler = logging.FileHandler("data.log", encoding="utf-8")
    filehandler.setFormatter(myformat)

    mylog.addHandler(consoleHandler)
    mylog.addHandler(filehandler)
    mylog.info("tset")

if __name__ == '__main__':
    main()
