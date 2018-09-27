# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    rent_type = scrapy.Field()
    house_type = scrapy.Field()
    area = scrapy.Field()
    towards = scrapy.Field()
    floor = scrapy.Field()
    decoration = scrapy.Field()
    building_type = scrapy.Field()
    community = scrapy.Field()