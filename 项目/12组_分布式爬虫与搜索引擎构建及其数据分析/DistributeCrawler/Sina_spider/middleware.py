# encoding=utf-8


import logging
import random

import pymongo

from user_agents import agents

logger = logging.getLogger(__name__)


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookieMiddleware(object):
    """
    每次请求都随机从账号池中选择一个账号去访问
    """
    def __init__(self):
        client = pymongo.MongoClient("mongo", 27017)
        self.account_collection = client["accounts"]['account']

    def process_request(self, request, spider):
        all_count = self.account_collection.find({'status': 'success'}).count()
        if all_count == 0:
            raise Exception('当前账号池为空')
        random_index = random.randint(0, all_count - 1)
        random_account = self.account_collection.find({'status': 'success'})[random_index]
        request.headers.setdefault('Cookie', random_account['cookie'])
        request.meta['account'] = random_account
        print "此次请求使用的账号为：" + random_account['_id']


class ListCookieMiddleware(object):
    """
    每次请求都随机从账号池中选择一个账号去访问
    """
    def __init__(self):
        client = pymongo.MongoClient("mongo", 27017)
        self.account_collection = client["accounts"]['account']
        self.countt = 50

    def process_request(self, request, spider):
        all_count = self.account_collection.find({'status': 'success'}).count()
        if all_count == 0:
            raise Exception('当前账号池为空')
        self.countt -= 1
        random_account = self.account_collection.find({'status': 'success'})[self.countt]
        request.headers['Cookie'] = random_account['cookie']
        request.meta['account'] = random_account


class RedirectMiddleware(object):
    """
    检测账号是否正常
    302 / 403,说明账号cookie失效/账号被封，状态标记为error
    418,偶尔产生,需要再次请求
    """
    def __init__(self):
        client = pymongo.MongoClient("mongo", 27017)
        self.account_collection = client["accounts"]['account']

    def process_response(self, request, response, spider):
        http_code = response.status
        if http_code == 302 or http_code == 403:
            self.account_collection\
                .find_one_and_update\
                ({'_id': request.meta['account']['_id']}, {'$set': {'status': 'error'}}, )
            return request
        elif http_code == 418:
            spider.logger.error('该IP已被限制请求，请更换ip。')
            return request
        else:
            return response
