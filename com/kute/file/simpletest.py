#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/17 20:42'

"""

"""

import os

_resources_dir = os.path.join(os.path.dirname(__file__), "resources")


def getfilepath(filename):
    return os.path.join(_resources_dir, filename)


# 读文件内容
def read_file():
    filepath = getfilepath("urls.txt")
    with open(file=filepath, mode="r") as f:
        for line in f:
            # print(line)
            # write_by_line(line)
            write_list_lines(f.readlines())


# 按行写入
def write_by_line(line):
    with open(file=getfilepath("writefile.txt"), mode="a") as f:
        f.write(line)


# 按批写入
def write_list_lines(lines):
    with open(file=getfilepath("writefile.txt"), mode="a") as f:
        f.writelines(lines)


def main():
    read_file()


if __name__ == '__main__':
    main()
