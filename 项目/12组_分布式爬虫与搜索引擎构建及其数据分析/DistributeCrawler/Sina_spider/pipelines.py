# encoding=utf-8

import pymongo
from items import InformationItem, TweetsItem, RelationshipsItem
import MySQLdb


class ElasticsearchPipeline(object):
    # 将数据写入到es中
    def process_item(self, item, spider):
        item.save_to_es()
        return item

class MongoDBPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("mongo", 27017)
        db = clinet["Sina"]
        self.Information = db["Information"]
        self.Tweets = db["Tweets"]
        self.Relationships = db["Relationships"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, RelationshipsItem):
            try:
                self.Relationships.insert(dict(item))
            except Exception:
                pass
        elif isinstance(item, TweetsItem):
            try:
                self.Tweets.insert(dict(item))
            except Exception:
                pass
        elif isinstance(item, InformationItem):
            try:
                self.Information.insert(dict(item))
            except Exception:
                pass
        return item