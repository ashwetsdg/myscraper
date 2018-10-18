# -*- coding: utf-8 -*-
import scrapy
import re
import json

class MvideoSpider(scrapy.Spider):
    name = 'mvideo'
    allowed_domains = ['mvideo.ru']
    start_urls = [
        'https://www.mvideo.ru/apple/iphone',
        'https://www.mvideo.ru/stiralnye-i-sushilnye-mashiny-2427'
        'https://www.mvideo.ru/apple/ipad',
        'https://www.mvideo.ru/apple/mac'
    ]

    def parse(self, response):
        urls = response.css(
            '.c-preview-article__text p a::attr(href)'
        ).extract()
        if urls:
            for u in urls:
                yield response.follow(u, callback=self.parse_price)
            return

        urls = response.css(
            '.category-grid-item-link::attr(href)'
        ).extract()
        if urls:
            for u in urls:
                yield response.follow(u, callback=self.parse_price)
            return


    def parse_price(self, response):
        data = response.css(
            '.sel-product-tile-title::attr(data-product-info)'
        ).extract()
        for item in data:
            #yield {'id': id, 'price' price}
            yield json.loads(item)

