# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem


class TutorialPipeline(object):
    def process_item(self, item, spider):
        """过滤掉不合法的item
        """
        if item['url']:
            return item
        else:
            # 抛出异常, 将此item丢弃, 则不会传递给其他pipeline
            raise DropItem("useless item[{}] and then being droped and will not pass to next pipeline.".format(item))

    def open_spider(self, spider):
        print('invoke when spider is opened.')

    def close_spider(self, spider):
        print('invoke when spider is closed.')
