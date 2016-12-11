#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/12/11 10:30'

"""

系统平台参数

"""

import platform
import logging
import sys


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')
log = logging.getLogger(__name__)


def main():
    log.info(platform.architecture())  # 32 or 64 bit
    log.info(sys.maxsize > 2 ** 32)  # is 64 bit
    log.info(platform.libc_ver())
    log.info(platform.mac_ver())
    log.info(platform.machine())
    log.info(platform.uname())
    log.info(platform.system())  # Darwin   Windows  Linux
    log.info(platform.release())

    log.info(platform.java_ver())  # for Jython

    # python info
    log.info(platform.python_version())
    log.info(platform.python_version_tuple())
    log.info(platform.python_build())


if __name__ == '__main__':
    main()
