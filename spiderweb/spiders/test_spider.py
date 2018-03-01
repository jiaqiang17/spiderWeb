# -*- coding: utf-8 -*-
import scrapy
from spiderweb.items import TestItem

class TestSpider(scrapy.spiders.Spider):
    name = "test"
    allowed_domains= ["www.proginn.com/users/"]

    def start_requests(self):
        pages = []
        for i in range(1, 10):
            url = 'https://www.proginn.com/%s' % i
            page = scrapy.Request(url)
            pages.append(page)
        return pages

    def parse(self, response):

        filename = "testFile1.html"
        with open(filename, "wb") as f:
            for sel in response.xpath('//*[@class="title"]'):
                if sel.xpath('a/@userid').extract():
                    item = TestItem()
                    item['title'] = sel.xpath('a/text()').extract()
                    item['href'] = sel.xpath('a/@href').extract()
                    item['userid'] = sel.xpath('a/@userid').extract()
                    yield item
            f.write(response.body)




