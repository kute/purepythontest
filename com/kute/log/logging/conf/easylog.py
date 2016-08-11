#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/10 21:29'

"""

将 com.kute.log.logging.conf 这个package整个放到 你的site-packages里，随意起个名称
例如easylog，然后以后就可以直接用了
参加：test.testeasylog.py

"""
import os
import logging
from logging import config


_resources_dir = os.path.join(os.path.dirname(__file__), 'resources')

_easylog_conf_path = os.path.join(_resources_dir, 'easylog.conf')

config.fileConfig(_easylog_conf_path)


def geteasylog():
    return logging.getLogger("easylog")


def main():
    easylog = geteasylog()
    easylog.info("this is a easy log.")
    easylog.info("tt")


if __name__ == '__main__':
    main()
