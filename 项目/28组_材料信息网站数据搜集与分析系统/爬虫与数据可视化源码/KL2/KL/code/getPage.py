# encoding:utf-8
# Author:GROUP 1
# Version:2.0.0 建立通用爬取模块 2019.10.18

import requests
from lxml import etree
from KL.code.getCookie import getCookie
import time
from KL.code.categories import *
from KL.code.parsePage import *
from pymongo import MongoClient

client=MongoClient('localhost',27017)
database=client['project']
URL_data =database['URL']

header = {
    "Connection": "keep-alive",
    "Host": "www.pfchina.com.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}


# 请求html，并返回html源码
def requestPage(tail):
    pageBase = "http://www.pfchina.com.cn"
    page = requests.get(pageBase + tail, headers=header)
    page.encoding = 'gbk'
    # ############################################################测试使用。打印每个页面title 不需要时注释掉后面三条语句
    pageHtml = etree.HTML(page.text)
    title = pageHtml.xpath("/html/body/div[5]/div[1]/div[1]/h1//text()")[0]
    print(title)
    return page.text


# 获取CPP日评页面  返回'-1'为失败。若成功则返回更新条数。
def getPage(cookie, kind):
    # 传入参数
    listBase = "http://www.pfchina.com.cn/scripts/TitleSearch.asp?colno=" + kind.number + "&pagesize=25&Keyword=&Page="
    urlNum = 0  # url数
    header["Cookie"] = cookie
    countTimeout = 0
    while 1:
        try:
            listPage = requests.get("http://www.pfchina.com.cn/titlefile/" + kind.number + ".asp", headers=header)
            break
        except TimeoutError:  # 网络出现问题的处理：23秒后重新尝试连接，超过五次连不上认为网络错误。（为什么是23秒呢，因为随便按了两个数）
            countTimeout += 1
            if countTimeout > 5:
                print("网络错误。")
                return '-1'
            else:
                print("请求超时,等待重新连接...")
                time.sleep(23)
    listPage.encoding = 'gbk'


    isNew = 1
    newTail = None

    if URL_data.find_one({"kind": kind.id}) is not None:
        # 取数据库tail
        old_tail = URL_data.find_one({"kind": kind.id}).get("tail")
    else:
        old_tail = None


    page = etree.HTML(listPage.text)
    stop = 0
    pageNum = int(page.xpath("/html/body/div[3]/div[2]/div/font[2]/text()")[0])  # 总页数
    # print(pageNum)  # ##############################################################################测试使用。打印总页数
    for curPage in range(1, pageNum+1):
        listPage = requests.get(listBase + str(curPage), headers=header)  # 得到list的页面不同
        listPage.encoding = 'gbk'
        listHtml = etree.HTML(listPage.text)
        # text包含所需条目的href值
        xpath = r"/html/body/div[6]/div[2]/ul/li//a"
        list_ = listHtml.xpath(xpath + "[re:match(@title,'.*" + kind.keywords + ".*')]//@href",
                               namespaces={"re": "http://exslt.org/regular-expressions"})

        for tail in list_:

            if tail == old_tail:
                stop = 1
                break

            page = requestPage(tail)
            if page == '-1':
                print("网络异常，停止更新。")
                break
            parsePage(page, kind)

            if isNew == 1:
                newTail = tail
                isNew = 0

            urlNum += 1
            print(urlNum)  # ######################################################################测试使用。打印当前是第几条

        if stop == 1:
            break

    if old_tail is not None and newTail is not None:
        condition = {"kind": kind.id}
        result = URL_data.find_one({"kind": kind.id})
        result['tail'] = newTail
        URL_data.update(condition, result)
    elif old_tail is None and newTail is not None:
        data = {
            "kind": kind.id,
            "tail": newTail
        }
        URL_data.insert_one(data)

    # 打印目前抓取完的条数
    print(kind.keywords + "更新" + str(urlNum) + "条")
    return urlNum


