# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from cat.items import CatItem


class CatSpiderSpider(scrapy.Spider):
    name = 'cat_spider'
    allowed_domains = ['www.ivsky.com']
    start_urls = ['https://www.ivsky.com/tupian/maomi_t178/']

    def parse(self, response):
        cats = response.xpath('//ul[@class="pli"]/li/div/a/img')
        for cat in cats:
            loader = ItemLoader(item=CatItem())
            image_url = cat.xpath('.//@src').extract_first()
            image_url = response.urljoin(image_url)
            loader.add_value('image_urls', image_url)
            yield loader.load_item()

        next_page = response.xpath('//a[@class="page-next"]/@href').get()
        if next_page:
            yield response.follow(response.urljoin(next_page), callback=self.parse)
