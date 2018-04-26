# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_tv.items import ScrapyTvItem
from scrapy import Selector

class goudaiTV_spider(RedisCrawlSpider):
    name = 'goudaiTV_spider'
    redis_key = 'goudaiTV_spider:start_urls'
    allowed_domains = ['goudaitv.com']
    rules = [
        Rule(link_extractor=LinkExtractor(allow='index[0-9]*-pg-[0-9]*\.html'),callback='parse_func',follow=True),
    ]

    def parse_func(self,response):
        for i in response.xpath('//*[@id="data_list"]/li[*]/div/a'):
            yield {
			'name' : '狗带TV-'+''.join(i.xpath('span[2]/text()').extract()),
            'url' : "http://www.yibuyy.com"+''.join(i.xpath('@href').extract())
			}
