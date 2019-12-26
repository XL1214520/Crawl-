# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class JianshuItem(Item):
    # 标题
    title = Field()
    # 作者头像
    avatar = Field()
    # 作者ID
    author = Field()
    # 文章地址
    origin_url = Field()
    # 文章ID
    article_id = Field()
    # 文章内容
    content = Field()
    # 文章字数
    word_count = Field()
    # 浏览量
    view_count = Field()
    # 评论数
    comment_count = Field()
    # 喜欢数
    like_count = Field()