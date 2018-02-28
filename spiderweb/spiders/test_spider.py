# -*- coding: utf-8 -*-
import scrapy
from pymongo import MongoClient
from spiderweb.items import TestItem

class TestSpider(scrapy.spiders.Spider):
    name = "test"
    allowed_domains= ["www.proginn.com/users/"]
    start_urls = [
        "https://www.proginn.com/users/"
    ]

    def parse(self, response):

        self.connectMongo()
        filename = "testFile1.html"
        with open(filename, "wb") as f:
            for sel in response.xpath('//a'):
                item = TestItem()
                item['title'] = sel.xpath('text()').extract()
                item['href'] = sel.xpath('@href').extract()
                yield item
                print(item['title'], " --- ", item['href'])


            f.write(response.body)



    def connectMongo(self):
        # 建立MongoDB数据库连接
        client = MongoClient('localhost', 27017)
        # 连接所需数据库,test为数据库名
        db = client.test
        # 连接所用集合，也就是我们通常所说的表，test为表名
        collection = db.test
        # 查找集合中单条数据
        print(collection.find_one())
