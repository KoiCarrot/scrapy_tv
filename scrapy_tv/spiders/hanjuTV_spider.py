# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_tv.items import ScrapyTvItem
from scrapy import Selector

class hanjuTV_spider(RedisCrawlSpider):
    name = 'hanjuTV_spider'
    redis_key = 'hanjuTV_spider:start_urls'
    allowed_domains = ['hanju.cc']
    rules = [
        Rule(link_extractor=LinkExtractor(allow='list_8_[1-9][0-9]?\.html'),callback='parse_func',follow=True),
    ]

    def parse_func(self,response):
        for i in response.xpath('//*[@class="stab-con"]/dl/dd/li'):
            yield {
			'name':'韩剧TV-'+''.join(i.xpath('div[1]/span/a/b/text()').extract()),
            'url':'http://www.hanju.cc' + ''.join(i.xpath('a/@href').extract())
			}
