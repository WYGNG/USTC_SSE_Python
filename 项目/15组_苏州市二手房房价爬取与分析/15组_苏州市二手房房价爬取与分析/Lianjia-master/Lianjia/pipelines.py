# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class LianjiaPipeline(object):
    def __init__(self):
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        dbname = settings['MONGO_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.coll = mydb[settings['MONGO_COLL']]
        # self.items = {}

    def process_item(self, item, spider):
        data = dict(item)
        # # self.items.update(data)
        # if self.coll.find_one({"url_token": data['url_token']}):
        #     self.coll.update_one({'url_token': data['url_token']}, {"$set": data}, upsert=True)
        # else:
        #     self.coll.insert(data)
        self.coll.insert(data)
        # print('this is pipelines')
        return item
