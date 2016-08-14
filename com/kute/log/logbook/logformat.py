#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: logformat.py
@ __mtime__: 2016/8/12 19:07

日志格式 测试

配置日志格式两种方式：
a) 传 格式 字符串
b）hook format function

"""

from logbook import StreamHandler, info
import sys

# 1. set format_string
sh = StreamHandler(sys.stdout,
                   format_string="[{record.time}] {record.level_name}: {record.channel}：{record.message}")

# 2. set format_string
sh.format_string = "[{record.time}] {record.level_name}: {record.channel}：{record.message}"


# 3. invoke the format function
def my_format_fun(record, handler):
    return " ".join(["[" + str(record.time) + "]", record.level_name + "：" + record.channel + "：", record.message])
sh.formatter = my_format_fun


def main():
    info("test")


if __name__ == "__main__":
    with sh.applicationbound():
        main()
