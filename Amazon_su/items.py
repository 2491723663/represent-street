# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazontestItem(scrapy.Item):
    # define the fields for your item here like:
     asin = scrapy.Field()
     url  = scrapy.Field()
     rank_big = scrapy.Field()
     rank_small = scrapy.Field()


class AmazonRecordItem(scrapy.Item):
    asin = scrapy.Field()
    url = scrapy.Field()
    rank_big = scrapy.Field()
    rank_small = scrapy.Field()