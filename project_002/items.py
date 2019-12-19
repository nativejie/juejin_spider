# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Project002Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    like = scrapy.Field()
    user = scrapy.Field()
    category = scrapy.Field()
    updated_date = scrapy.Field()
    article_id = scrapy.Field()
    pass
