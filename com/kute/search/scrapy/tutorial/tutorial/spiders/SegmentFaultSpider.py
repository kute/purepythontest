#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/26 10:34'

"""

"""

import scrapy
from ..items import SegmentFaultItem
from ..itemloader import SegmentFaultItemLoader


class SegmentFaultSpider(scrapy.Spider):
    name = 'segmentfaultspider'
    allowed_domains = ['segmentfault.com']
    start_urls = [
        "https://segmentfault.com/questions?page=2"
    ]

    def parse(self, response):
        for sel in response.xpath("//section"):
            # Item Loader在每个(Item)字段中都包含了一个输入处理器和一个输出处理器
            loader = SegmentFaultItemLoader(item=SegmentFaultItem(), response=response)
            loader.add_value('title', sel.xpath("div[@class='summary']/h2/a/text()").extract())
            loader.add_value('url', "".join(["https://segmentfault.com", sel.xpath("div[@class='summary']/h2/a/@href")[0].extract()]))
            loader.add_value('author', sel.xpath("div[@class='summary']/ul[@class='author list-inline']//a[1]/text()").extract())
            loader.add_value('tags', sel.xpath("div[@class='summary']/ul[@class='taglist--inline ib']//a/text()").extract())
            loader.add_value('createtime', sel.xpath("div[@class='summary']/ul[@class='author list-inline']//a[2]/text()").extract())
            loader.add_value('vote', sel.xpath("div[@class='qa-rank']/div[contains(@class, 'votes')]").re("\d"))
            loader.add_value('answer', sel.xpath("div[@class='qa-rank']/div[contains(@class, 'answers')]").re("\d"))
            loader.add_value('view', sel.xpath("div[@class='qa-rank']/div[contains(@class, 'views')]/span/text()").extract())
            yield loader.load_item()


def main():
    print("".join(['a', 'b']))


if __name__ == '__main__':
    main()
