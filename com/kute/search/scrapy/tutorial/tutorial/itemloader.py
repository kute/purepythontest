#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/27 21:33'

"""

"""

from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, MapCompose, TakeFirst
from .constant import unit_dict


def to_number(origin):
    """
    1.9k to 1900
    """
    if any(map(lambda e: e in origin, ['k', 'K', 'w', 'W'])):
        length = len(origin)
        return int(float(origin[0: length - 1]) * unit_dict[origin[length - 1:]])
    else:
        return origin


class SegmentFaultItemLoader(ItemLoader):
    default_input_processor = Identity()
    default_output_processor = Identity()

    title_out = TakeFirst()
    url_out = TakeFirst()
    author_out = TakeFirst()
    vote_out = MapCompose(TakeFirst(), to_number)
    answer_out = MapCompose(TakeFirst(), to_number)
    view_out = MapCompose(TakeFirst(), to_number)
    createtime_out = TakeFirst()


def main():
    print(to_number("1.9W"))


if __name__ == '__main__':
    main()
