#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/27 21:33'

"""

Item Loader Context : 传递修改 额外的数据

"""

from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, MapCompose, TakeFirst
from .constant import to_number, add_unit


class SegmentFaultItemLoader(ItemLoader):
    default_input_processor = Identity()
    default_output_processor = Identity()

    title_out = TakeFirst()
    url_out = TakeFirst()
    author_out = TakeFirst()
    vote_out = MapCompose(TakeFirst(), to_number, add_unit)
    answer_out = MapCompose(TakeFirst(), to_number, add_unit)
    view_out = MapCompose(TakeFirst(), to_number, add_unit)
    createtime_out = TakeFirst()


def main():
    print(to_number("1.9W"))


if __name__ == '__main__':
    main()
