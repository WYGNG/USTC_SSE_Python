# encoding=utf-8
import pickle

from scrapy import Item, Field

from Sina_spider.es_types import InformationType, TweetsType, RelationshipsType


class InformationItem(Item):

    """ 个人信息 """
    _id = Field()  # 用户ID
    NickName = Field()  # 昵称
    Gender = Field()  # 性别
    Province = Field()  # 所在省
    City = Field()  # 所在城市
    BriefIntroduction = Field()  # 简介
    Birthday = Field()  # 生日
    Num_Tweets = Field()  # 微博数
    Num_Follows = Field()  # 关注数
    Num_Fans = Field()  # 粉丝数
    SexOrientation = Field()  # 性取向
    Sentiment = Field()  # 感情状况
    VIPlevel = Field()  # 会员等级
    Authentication = Field()  # 认证
    URL = Field()  # 首页链接
    def save_to_es(self):
        es_info = InformationType()
        es_info.initz(self)
        es_info.save(index="info")

class TweetsItem(Item):
    """ 微博信息 """
    _id = Field()  # 用户ID-微博ID
    ID = Field()  # 用户ID
    Content = Field()  # 微博内容
    PubTime = Field()  # 发表时间
    Co_oridinates = Field()  # 定位坐标
    Tools = Field()  # 发表工具/平台
    Like = Field()  # 点赞数
    Comment = Field()  # 评论数
    Transfer = Field()  # 转载数
    def save_to_es(self):
        es_info = TweetsType()
        es_info.initz(self)
        es_info.save(index="tweets")

class RelationshipsItem(Item):
    """ 用户关系，只保留与关注的关系 """
    Host1 = Field()
    Host2 = Field()  # 被关注者的ID
    def save_to_es(self):
        es_info = RelationshipsType()
        es_info.initz(self)
        es_info.save(index="rel")
