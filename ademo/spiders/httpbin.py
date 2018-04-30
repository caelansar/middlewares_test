# -*- coding: utf-8 -*-
import scrapy

from ..items import AdemoItem


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        item = AdemoItem()
        item['url'] = response.url
        self.logger.debug(response.status)
        self.logger.debug(response.text)
        yield item
