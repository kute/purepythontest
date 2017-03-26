# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import os


class SegmentFaultItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    vote = scrapy.Field()
    answer = scrapy.Field()
    view = scrapy.Field()
    createtime = scrapy.Field()


if __name__ == '__main__':
    print(os.path.join("aa", 'bb'))
