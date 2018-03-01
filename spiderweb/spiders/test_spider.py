# -*- coding: utf-8 -*-
import scrapy
from spiderweb.items import TestItem

class TestSpider(scrapy.spiders.Spider):
    name = "test"
    allowed_domains= ["www.proginn.com/users/"]
    start_urls = [
        "https://www.proginn.com/users/"
    ]

    def parse(self, response):

        filename = "testFile1.html"
        with open(filename, "wb") as f:
            for sel in response.xpath('//a'):
                item = TestItem()
                item['title'] = sel.xpath('text()').extract()
                item['href'] = sel.xpath('@href').extract()
                yield item
            f.write(response.body)




