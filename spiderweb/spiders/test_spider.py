# -*- coding: utf-8 -*-
import scrapy
from spiderweb.items import TestItem

class TestSpider(scrapy.spiders.Spider):
    name = "test"

    def start_requests(self):
        pages = []
        for i in range(1, 1001):
            url = 'https://www.proginn.com/%s' % i
            page = scrapy.Request(url)
            pages.append(page)
        return pages

    def parse(self, response):

        filename = "testFile1.html"
        with open(filename, "wb") as f:
            for sel in response.xpath('//div[@class="item J_user"]//div[@class="title"]'):
                if sel.xpath('a/@href').extract()[0] != '/hire/fast':
                    item = TestItem()
                    item['title'] = sel.xpath('a/span[1]/text()').extract()[0].strip() + "  " + sel.xpath('a/span[2]/text()').extract()[0].strip()
                    item['href'] = sel.xpath('a/@href').extract()[0]
                    item['userid'] = sel.xpath('a/@userid').extract()[0]
                    yield item
            f.write(response.body)




