# -*- coding: utf-8 -*-
import scrapy
import json
import re
from Lianjia.items import LianjiaItem
from scrapy_redis.spiders import RedisSpider

class LianjiaSpider(RedisSpider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    redis_key = 'lianjia:start_urls'
    # start_urls = ['https://su.lianjia.com/ershoufang/pg1/']

    base_url = 'https://su.lianjia.com'


    def parse(self, response):
        area_url = response.xpath('//div[@data-role="ershoufang"]/div[1]/a/@href').extract()
        for url in area_url:
            yield scrapy.Request(url=self.base_url + url, callback=self.parse_region)

    def parse_region(self, response):
        local_url = response.xpath('//div[@data-role="ershoufang"]/div[2]/a/@href').extract()
        for url in local_url:
            yield scrapy.Request(url=self.base_url + url + 'pg1/', callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        total_page = json.loads(response.xpath('//div[@class="page-box fr"]/div[1]/@page-data').extract()[0])[
            "totalPage"]
        if total_page:
            for i in range(1, total_page + 1):
                yield scrapy.Request(url=response.url[:-2] + str(i) + '/', callback=self.parse_detail)

    def parse_detail(self, response):
        detail_url = response.xpath('//div[@class="title"]/a/@href').extract()
        for url in detail_url:
            yield scrapy.Request(url=url, callback=self.parse_item)


    def parse_item(self, response):
        item = LianjiaItem()

        item['title'] = response.xpath('//h1/@title').extract()[0]

        item['house_type'] = re.findall(r"houseType:'(.*?)',", response.text)[0]
        item['position'] = re.findall(r"resblockPosition:'(.*?)',", response.text)[0]
        item['longitude'] = item['position'].split(',')[0]
        item['latitude'] = item['position'].split(',')[1]

        item['area'] = re.findall(r"area:'(.*?)',", response.text)[0]
        item['total_price'] = re.findall(r"totalPrice:'(.*?)',", response.text)[0]
        item['avg_price'] = re.findall(r"price:'(.*?)',", response.text)[0]
        item['community'] = re.findall(r"resblockName:'(.*?)',", response.text)[0]

        base_datail = response.xpath('//*[@id="introduction"]//ul/li/text()').extract()
        item['layout'] = base_datail[0]
        item['floor'] = base_datail[1]
        # item['area'] = base_datail[2][:-1]


        if item['house_type'] == '别墅':
            item['direction'] = base_datail[4]
            item['decorate'] = base_datail[6]

        else:
            item['design'] = base_datail[3]
            item['direction'] = base_datail[6]
            item['decorate'] = base_datail[8]
            item['lift'] = base_datail[10]
            item['lift_proportion'] = base_datail[9]

        # item['total_price'] = response.xpath('//span[@class="total"]/text()').extract()[0]
        # item['avg_price'] = response.xpath('//span[@class="unitPriceValue"]/text()').extract()[0]


        item['region'] = response.xpath('//span[@class="info"]/a[1]/text()').extract()[0]
        item['local'] = response.xpath('//span[@class="info"]/a[2]/text()').extract()[0]
        # item['community'] = response.xpath('//div[@class="communityName"]/a[1]/text()').extract()[0]

        yield item