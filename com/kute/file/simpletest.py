#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/17 20:42'

"""

"""

import os
import codecs
import fileinput

_resources_dir = os.path.join(os.path.dirname(__file__), "resources")


def getfilepath(filename):
    return os.path.join(_resources_dir, filename)


# 读文件内容
def read_file():
    filepath = getfilepath("urls.txt")
    with open(file=filepath, mode="r") as f:
        # for line in f:
        for i in range(20):
            # print(line)
            # write_by_line(line)
            write_list_lines(f.readlines())


# 按行写入
def write_by_line(line):
    with open(file=getfilepath("writefile.txt"), mode="a") as f:
        f.write(line)


# 按批写入
def write_list_lines(lines):
    with open(file=getfilepath("writefile.txt"), mode="w") as f:
        f.writelines(lines)


# 自动转换文件编码读取内容
def read(file):
    with codecs.open(file, 'r', 'utf-8') as bf:
        print(bf.read())


def read_user_input():
    with fileinput.input() as f:
        for line in f:
            print(line, f.filename(), f.lineno())


def main():
    # read_file()
    read_user_input()


if __name__ == '__main__':
    main()
