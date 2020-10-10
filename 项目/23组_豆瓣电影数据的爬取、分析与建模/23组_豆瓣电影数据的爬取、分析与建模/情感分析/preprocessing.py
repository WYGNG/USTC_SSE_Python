#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import langconv
import jieba
import sys


class TextPreprocessor(object):

    def __init__(self, text=None, stopword_file=None):
        """
        stopword_file='data/stopwords/stopword_normal.txt'
        """
        self.text = text
        self.stopwords = self.init_stopwords(stopword_file)

    def init_stopwords(self, filepath):
        """
        初始化停留词
        """
        if filepath == None:
            return []
        stopwords = [line.strip() for line in open(filepath, encoding='UTF-8').readlines()]
        return stopwords

    def process_line(self, text):
        """
        文本数据处理，返回关键字list
        """
        text = self.traditional2simplified(text)
        text = self.word_replace(text)
        text = self.filter_trim(text)
        tokenizer = self.remove_stopword(text)
        return tokenizer

    def traditional2simplified(self, text):
        """
            将sentence中的繁体字转为简体字
            param: text
            return: 繁体字转换为简体字之后的文本
        """
        if text == "":
            return text
        text = langconv.Converter('zh-hans').convert(text)
        return text

    def word_replace(self, text):
        """
        词语替换
        """
        return text

    def filter_trim(self, text):
        """
        特殊符号过滤
        """
        # 去除换行符
        if text == "":
            return text
        reg = "[\r\n]+"
        text = re.sub(reg, '', text)
        # 去除特殊符号
        reg = "\\【.*】+|\\《.*》+|\\#.*#+|[./_$&%^*()<>+""'@|:~{}#]+|[0-9——\\=、：“”‘’￥……（）《》?【】\\[\\]a-z]+"
        text = re.sub(reg, '', text)
        reg = r"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]"
        text = re.sub(reg, '', text)
        return text

    def remove_stopword(self, text):
        """
        按照下面方式处理字符串
        1. 去除标点符号
        2. 去掉无用词
        3. 返回剩下的词的list
        """
        if text == "":
            return text
        ltext = jieba.lcut(text)
        res_text = []
        for word in ltext:
            if word not in self.stopwords:
                res_text.append(word)
        return res_text


if __name__ == "__main__":
    preprocessor = TextPreprocessor(stopword_file='./data/stopwords/stopword_normal.txt')
    test = "!@#$%^我不知道那时候为什么看了这么多香港口水片……[]"
    test = preprocessor.process_line(test)
    print(test)
