# -*- coding: utf-8 -*-
import scrapy
from spiderweb.items import GetdetailItem
from pymongo import MongoClient
from scrapy.conf import settings

class TestSpider(scrapy.spiders.Spider):
    name = "getdetail"  # 获取客栈里的所有有用的开发者的详细信息

    def start_requests(self):
        self.client = MongoClient(settings['MONGO_HOST'], settings['MONGO_PORT'])
        self.db = self.client[settings['MONGO_DB']]
        pages = []
        for item in self.db['users'].find():
            url = item['href']
            page = scrapy.Request(url)
            pages.append(page)
            print(url)
        return pages


    def parse(self, response):

        item = GetdetailItem()

        introduce = ""
        for sel in response.xpath('//div[@id="J_WoMainContent"]/div[1]//p'):
            introduce += sel.xpath('text()').extract()[0].strip()

        item['introduce'] = introduce
        yield item




