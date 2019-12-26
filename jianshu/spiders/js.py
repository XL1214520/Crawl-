# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem
import json,re

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    # 解析页面
    def parse_item(self, response):
        content = ''.join(response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/article//text()').extract())
        content = re.sub(r"[\n]",'',content)
        json_str = response.xpath('//*[@id="__NEXT_DATA__"]/text()').get()
        article_data = json.loads(json_str)
        title = article_data['props']['initialState']['note']['data']['public_title']
        avatar = article_data['props']['initialState']['note']['data']["share_image_url"]
        author = article_data['props']['initialState']['note']['data']['user']['slug']
        origin_url = response.url
        article_id = article_data['props']['initialState']['note']['data']['slug']

        word_count = article_data['props']['initialState']['note']['data']['wordage']
        view_count = article_data['props']['initialState']['note']['data']['views_count']
        comment_count = article_data['props']['initialState']['note']['data']['comments_count']
        like_count = article_data['props']['initialState']['note']['data']['likes_count']
        item = JianshuItem(
            title=title,
            avatar=avatar,
            origin_url=origin_url,
            article_id=article_id,
            author=author,
            content=content,
            word_count=word_count,
            view_count=view_count,
            comment_count=comment_count,
            like_count=like_count,
        )
        yield item