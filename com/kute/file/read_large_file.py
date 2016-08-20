#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: read_large_file.py
@ __mtime__: 2016/8/20 12:18

读取大文本数据

"""
import os
from kute.easylog.easylog import geteasylog
from kute.caltime.caltime import process_time
import fileinput


easylog = geteasylog()

_resources_dir = os.path.join(os.path.dirname(__file__), "resources")


def getfilepath(filename):
    return os.path.join(_resources_dir, filename)


def processline(line):
    pass


@process_time
def way_1(filepath):
    """
    按行读取单个文件
    """
    with open(filepath) as f:
        for line in f:
            # easylog.info(line)
            processline(line)


@process_time
def way_2(*args):
    """
    按行读取多个文件
    """
    for line in fileinput.input(files=args):
        # easylog.info(line)
        processline(line)


@process_time
def way_by_chunk(filepath, chunksize=1024):
    with open(filepath) as f:
        while True:
            piece = f.read(chunksize)
            if not piece:
                return
            yield piece


def main():
    filepath = getfilepath("writefile.txt")
    print(filepath)
    # way_1(filepath)

    # way_2(filepath)

    for piece in way_by_chunk(filepath):
        easylog.info(piece)


if __name__ == "__main__":
    main()
