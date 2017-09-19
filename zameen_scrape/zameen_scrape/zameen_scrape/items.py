# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZameenScrapeItem(scrapy.Item):

    title = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    bedrooms = scrapy.Field()
    area = scrapy.Field()
    phone = scrapy.Field()
    posted_on = scrapy.Field()
