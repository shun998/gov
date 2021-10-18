# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GovItem(scrapy.Item):
    # define the fields for your item here like:
    type = scrapy.Field()
    located = scrapy.Field()
    body = scrapy.Field()
    time = scrapy.Field()
    address = scrapy.Field()
    process = scrapy.Field()
    material = scrapy.Field()
    condition = scrapy.Field()
    method = scrapy.Field()
