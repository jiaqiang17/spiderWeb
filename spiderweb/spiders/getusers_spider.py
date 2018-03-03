# -*- coding: utf-8 -*-
import scrapy
from spiderweb.items import GetusersItem

class TestSpider(scrapy.spiders.Spider):
    name = "getusers"  # 获取客栈里的所有有用的开发者信息

    def start_requests(self):
        pages = []
        for i in range(1, 1001):
            url = 'https://www.proginn.com/%s' % i
            page = scrapy.Request(url)
            pages.append(page)
        return pages

    def parse(self, response):

        for sel in response.xpath('//div[@class="item J_user"]//div[@class="title"]'):
            if sel.xpath('a/@href').extract()[0] != '/hire/fast':
                item = GetusersItem()
                item['title'] = sel.xpath('a/span[1]/text()').extract()[0].strip() + "  " + \
                                sel.xpath('a/span[2]/text()').extract()[0].strip()
                item['href'] = sel.xpath('a/@href').extract()[0]
                item['userid'] = sel.xpath('a/@userid').extract()[0]
                yield item




