# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

from scrapy.conf import settings

class SpiderwebPipeline(object):

    def __init__(self):
        self.client = MongoClient(settings['MONGO_HOST'], settings['MONGO_PORT'])
        self.db = self.client[settings['MONGO_DB']]

    def process_item(self, item, spider):

        if spider.name == 'test':
            data = {
                'title': item['title'],
                'href': item['href']
            }


            self.db['test2'].insert_one(data)
            print(data)

        return item


