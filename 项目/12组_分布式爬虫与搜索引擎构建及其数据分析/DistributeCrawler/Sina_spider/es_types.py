# -*- coding: utf-8 -*-
__author__ = 'noble'

from elasticsearch_dsl import DocType, Date, Nested, Boolean, analyzer, Completion, Keyword, Text, Integer

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["es-client:9200"])

def dict_to_object(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    inst=Dict()
    for k,v in dictObj.items():
        inst[k] = dict_to_object(v)
    return inst

class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__
class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])


class TweetsType(DocType):
    def initz(self,  dictObj):
        inst = Dict()
        for k, v in dictObj.items():
            if k != "_id":
                self[k] = dict_to_object(v)
            else:
                self["id"] = dict_to_object(v)
        return self
    id = Keyword()
    ID = Keyword()
    Content = Text(analyzer="ik_max_word")
    PubTime = Keyword()
    Co_oridinates = Text(analyzer="ik_max_word")
    Tools = Keyword()
    Like = Integer()
    Comment = Integer()
    Transfer = Integer()
    class Meta:
        index = "Tweets"
        doc_type = "Tweets"



class InformationType(DocType):
    def initz(self,  dictObj):
        inst = Dict()
        for k, v in dictObj.items():
            if k != "_id":
                self[k] = str(dict_to_object(v))
            else:
                self["id"] = dict_to_object(v)
        return self
    id = Keyword()
    NickName = Keyword()
    Gender = Text()
    Province =Keyword()
    City = Keyword()
    BriefIntroduction = Text(analyzer="ik_max_word")
    Birthday = Text()
    Num_Tweets =Integer()
    Num_Follows = Integer()
    Num_Fans = Integer()
    SexOrientation = Text()
    Sentiment = Text()
    VIPlevel = Text()
    Authentication = Text()
    URL = Text()
    class Meta:
        index = "info"
        doc_type = "info"
class RelationshipsType(DocType):
    def initz(self,  dictObj):
        inst = Dict()
        for k, v in dictObj.items():
            self[k] = dict_to_object(v)
        return self
    Host1 = Keyword()
    Host2 = Keyword()  # 被关注者的ID
    class Meta:
        index = "rel"
        doc_type = "rel"



if __name__ == "__main__":
    TweetsType.init(index="tweets")
    InformationType.init(index="info")
    RelationshipsType.init(index="rel")