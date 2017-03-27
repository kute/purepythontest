#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/27 22:02'

"""

"""

from scrapy.exporters import JsonLinesItemExporter


class CustomJsonLinesItemExporter(JsonLinesItemExporter):
    """
    使用 -o 参数 存文件时 unicde 中文支持
    http://blog.csdn.net/u013571243/article/details/52698935
    """
    def __init__(self, file, **kwargs):
        super(CustomJsonLinesItemExporter, self).__init__(file, ensure_ascii=False, **kwargs)


def main():
    pass


if __name__ == '__main__':
    main()
