# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderwebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GetusersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    userid = scrapy.Field()
    pass


class GetdetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    introduce = scrapy.Field()
    pass