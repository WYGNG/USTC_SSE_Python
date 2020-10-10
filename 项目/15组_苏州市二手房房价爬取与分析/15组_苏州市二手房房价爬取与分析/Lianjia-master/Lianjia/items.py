# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()

    house_type = scrapy.Field()
    position = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()


    layout = scrapy.Field()
    floor = scrapy.Field()
    area = scrapy.Field()
    design = scrapy.Field()
    direction = scrapy.Field()
    decorate = scrapy.Field()
    lift = scrapy.Field()
    lift_proportion = scrapy.Field()

    total_price = scrapy.Field()
    avg_price = scrapy.Field()

    region = scrapy.Field()
    local = scrapy.Field()
    community = scrapy.Field()

