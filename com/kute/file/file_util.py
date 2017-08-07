#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: file_util.py
@ __mtime__: 2017/8/7 15:01

"""

import os


def get_dir(relative="..", target_dir="resources"):
        return os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), relative)), target_dir)


def get_sub_dir(dirname):
        return os.path.join(get_dir(), dirname)
