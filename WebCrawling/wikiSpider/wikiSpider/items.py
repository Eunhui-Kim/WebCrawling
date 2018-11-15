# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


# Scrapy의 Item객체 하나는 웹사이트 페이지 하나를 나타냄
# Field는 (url, content, header, image 등)을 표현함
class Article(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()


class HPage(Item):
    title = Field()
    link = Field()
    desc = Field()


