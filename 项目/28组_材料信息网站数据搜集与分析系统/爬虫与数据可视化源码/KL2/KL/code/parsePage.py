# encoding:utf-8
from KL.code.categories import *
import requests
from lxml import etree
from pymongo import MongoClient
import re
from datetime import datetime

from pymongo.errors import DuplicateKeyError

# 解析页面并入库。参数page是一个html页面；kind是类别，定义在categories里。
def parsePage(page, kind):
    html = etree.HTML(page)
    if kind.id=='1':
        parse_BOPPDay(html)
    elif kind.id=='2':
        parse_CPPDay(html)
    elif kind.id=='3':
        parse_BOPETDay(html)
    elif kind.id=='4':
        parse_BOPETWeek(html)
    elif (kind.id == '5'):
        parse_PPDpage(html)
    elif (kind.id == '6'):
        parse_PPZpage(html)
    elif (kind.id == '7'):
        parse_PEpage(html)


def parse_BOPPDay(html):
    # 爬取日评标题
    day_title = html.xpath('//div[@class="detail l bk1234"]/h1/text()')[0].strip()

    # 爬取日评更新时间
    day_time = re.search(r'(\d{2}\.\d{2}\.\d{2})', day_title).group(1)
    if day_time:
        # 统一日评更新时间格式（YYYY-MM-DD）
        day_time = '20' + day_time
        day_time = day_time.replace(".", "-")
    else:
        # 如果日评标题处更新时间为空，爬取另一定位点的日评更新时间
        re.search(r'(\d{4}\-\d{2}\-\d{2})',
                  html.xpath('//div[@class="detail l bk1234"]/div[@class="art01"]/text()')[0].strip()).group(1)

    # 爬取日评分析预测
    strings = html.xpath('//div[@class="art02 mar"]')[0].xpath('string(.)').strip()
    day_forecast = ''.join(re.search(r"(BOPP走势分析预测)(.*)", strings, re.DOTALL).group(2).strip().split())

    # 爬取日评表格内容
    table_rows = html.xpath('//div[@class="art02 mar"]//table/tbody/tr')
    if table_rows:

        product_name = table_rows[1].xpath('td[1]')[0].xpath('string(.)').strip()
        product_table_dict = {}

        for i in range(1, len(table_rows)):
            row = table_rows[i]
            if (i == 1):
                area = row.xpath('td[2]')[0].xpath('string(.)').strip()
                price = row.xpath('td[3]')[0].xpath('string(.)').strip()
                change = row.xpath('td[4]')[0].xpath('string(.)').strip()
                compare2lastWeek = row.xpath('td[5]')[0].xpath('string(.)').strip()
            else:
                area = row.xpath('td[1]')[0].xpath('string(.)').strip()
                price = row.xpath('td[2]')[0].xpath('string(.)').strip()
                change = row.xpath('td[3]')[0].xpath('string(.)').strip()
                compare2lastWeek = row.xpath('td[4]')[0].xpath('string(.)').strip()

            product_change_dict = {
                "价格": price,
                "日涨跌": change,
                "较上周同期": compare2lastWeek
            }
            product_table_dict[area] = product_change_dict


        BOPP_day_info = {
            "title": day_title,
            "datetime": day_time,
            "forecast": day_forecast,
            product_name: product_table_dict
        }
    else:
        # 如果价格表Table为空，仅保存日评网站其他数据
        BOPP_day_info = {
            "title": day_title,
            "datetime": day_time,
            "forecast": day_forecast,
        }

    BOPP_day.insert_one(BOPP_day_info)

def parse_CPPDay(html):
    # 日评标题
    day_title = html.xpath('//div[@class="detail l bk1234"]/h1/text()')[0].strip()
    print(day_title)

    # 日评更新时间
    day_time = re.search(r'(\d{2}\.\d{2}\.\d{2})', day_title).group(1)
    if day_time:
        day_time = '20' + day_time
        day_time = day_time.replace(".", "-")
    else:
        re.search(r'(\d{4}\-\d{2}\-\d{2})',
                  html.xpath('//div[@class="detail l bk1234"]/div[@class="art01"]/text()')[0].strip()).group(1)
    print(day_time)


    # 日评分析预测
    strings = html.xpath('//div[@class="art02 mar"]')[0].xpath('string(.)').strip()
    day_forecast = ''.join(re.search(r"(后市分析预测)(.*)", strings, re.DOTALL).group(2).strip().split())
    print(day_forecast)

    # 日评表格内容

    table_rows = html.xpath('//div[@class="art02 mar"]//table/tbody/tr')
    if table_rows:

        product_table_dict_1 = {}
        product_table_dict_2 = {}
        product_table_dict_3 = {}

        product_name_1 = table_rows[1].xpath('td[1]')[0].xpath('string(.)').strip()
        product_name_2 = table_rows[4].xpath('td[1]')[0].xpath('string(.)').strip()
        product_name_3 = table_rows[7].xpath('td[1]')[0].xpath('string(.)').strip()

        for i in range(1, len(table_rows)):
            row = table_rows[i]

            if (i == 1 or i==4 or i==7):
                area = row.xpath('td[2]')[0].xpath('string(.)').strip()
                price = row.xpath('td[3]')[0].xpath('string(.)').strip()
                change = row.xpath('td[4]')[0].xpath('string(.)').strip()
                compare2lastWeek = row.xpath('td[5]')[0].xpath('string(.)').strip()
                compare2lastMonth = row.xpath('td[6]')[0].xpath('string(.)').strip()
            else:
                area = row.xpath('td[1]')[0].xpath('string(.)').strip()
                price = row.xpath('td[2]')[0].xpath('string(.)').strip()
                change = row.xpath('td[3]')[0].xpath('string(.)').strip()
                compare2lastWeek = row.xpath('td[4]')[0].xpath('string(.)').strip()
                compare2lastMonth = row.xpath('td[5]')[0].xpath('string(.)').strip()


            product_change_dict = {
                "价格": price,
                "日涨跌": change,
                "较上周同期": compare2lastWeek,
                "较上月同期": compare2lastMonth
            }

            if (i < 4):
                product_table_dict_1[area] = product_change_dict
            elif (i < 7):
                product_table_dict_2[area] = product_change_dict
            else:
                product_table_dict_3[area] = product_change_dict

        CPP_day_info = {
            "title": day_title,
            "datetime": day_time,
            "forecast": day_forecast,
            product_name_1: product_table_dict_1,
            product_name_2: product_table_dict_2,
            product_name_3: product_table_dict_3
        }
    else:
        CPP_day_info = {
            "title": day_title,
            "datetime": day_time,
            "forecast": day_forecast,
        }
    print(CPP_day_info)
    CPP_day.insert_one(CPP_day_info)

def parse_BOPETDay(html):
    '''
    提取BOPET日评中 出现翔宇的价格，及 期货市场
    :param html:
    :return:
    '''
    #获取标题
    title=html.xpath('//div[@class="detail l bk1234"]/h1')[0].xpath('string(.)').strip()

    div_data=html.xpath('//div[@class="art02 mar"]')[0]
    #获取期货市场分析
    strings=div_data.xpath('string(.)').strip()
    try:
        futures_analysis=''.join(re.search(r"(期货市场|原油市场)(.*?)(PX市场|聚酯原料|聚酯切片市场|BOPET膜市)",strings,re.DOTALL).group(2).strip().split())
    except Exception as e:
        print(e)
        print('当天无期货市场信息')
        futures_analysis='无'
    #获取发表时间
    date_text=html.xpath('//div[@class="art01"]')[0].xpath('string(.)')
    date=re.search(r'更新时间[:：](.*?)来源',date_text).group(1).strip()
    today = re.search(r'(\d+).(\d+).(\d+)', title)
    if today == None:
        today = date.split()[0];
    else:
        today='20{}-{}-{}'.format(today.group(1),today.group(2),today.group(3))
    table_rows=div_data.xpath('.//table/tbody/tr')
    if table_rows:
        product_name=''
        price_list={}
        # yesterday=table_rows[0].xpath('td[3]')[0].xpath('string(.)').strip()
        # today=table_rows[0].xpath('td[4]')[0].xpath('string(.)').strip()
        for row in table_rows[1:]:
            td_nums=len(row.xpath('td'))
            if td_nums==6:
                product_td=row.xpath('td[1]')[0]
                product_name=row.xpath('td[1]')[0].xpath('string(.)').strip()
                if re.match("绍兴翔宇",row.xpath('td[2]')[0].xpath('string(.)').strip()):
                    company=row.xpath('td[2]')[0].xpath('string(.)').strip()
                    #price_lastDay=row.xpath('td[3]')[0].xpath('string(.)').strip()
                    price_today=row.xpath('td[4]')[0].xpath('string(.)').strip()
                    change=row.xpath('td[5]')[0].xpath('string(.)').strip()
                    try:
                        remark=row.xpath('td[6]')[0].xpath('string(.)').strip()
                    except:
                        remark=''
                    row_dict={
                          'price':price_today,
                          '涨跌幅':change,'备注':remark
                          }
                    price_list[product_name] = row_dict
                    print(row_dict)
            else:
                if re.match("绍兴翔宇",row.xpath('td[1]')[0].xpath('string(.)').strip()):
                    company = row.xpath('td[1]')[0].xpath('string(.)').strip()
                    #price_lastDay = row.xpath('td[2]')[0].xpath('string(.)').strip()
                    price_today = row.xpath('td[3]')[0].xpath('string(.)').strip()
                    change = row.xpath('td[4]')[0].xpath('string(.)').strip()
                    try:
                        remark = row.xpath('td[5]')[0].xpath('string(.)').strip()
                    except:
                        remark = ''
                    row_dict = {
                                 'price':price_today,
                                '涨跌幅': change, '备注': remark
                                }
                    price_list[product_name] = row_dict
        print({
              'date':today,
              'title':title,
              '绍兴翔宇':price_list,
              'BOPET_futures_analysis':futures_analysis,
              'spider_time':datetime.now()
              })
        try:
            BOPET_day.insert_one({'_id':date,
                                  'date':today,
                                  'title':title,
                                  '绍兴翔宇':price_list,
                                  'BOPET_futures_analysis':futures_analysis,
                                  'spider_time':datetime.now()
                                  })
        except DuplicateKeyError as e:
            print(e)
            print('数据库中已存在该数据')
    else:
        if futures_analysis!='' or futures_analysis!="无" or futures_analysis!="无。":
            try:
                print({
                    'date': today,
                    'title': title,
                    'BOPET_futures_analysis': futures_analysis,
                    'spider_time': datetime.now()
                })
                BOPET_day.insert_one({'_id': date,
                                      'date':today,
                                      'title':title,
                                      'BOPET_futures_analysis': futures_analysis,
                                      'spider_time': datetime.now()
                                      })
            except DuplicateKeyError as e:
                print(e)
                print('数据库中已存在该数据')

def parse_BOPETWeek(html):
    '''

    爬取绍兴翔宇的相关价格信息
    及 BOPET膜市 的内容
    :param html:
    :return:
    '''
    title=html.xpath('//div[@class="detail l bk1234"]/h1')[0].xpath('string(.)').strip()

    date_text = html.xpath('//div[@class="art01"]')[0].xpath('string(.)')
    date = ' '.join(re.search(r'更新时间[:：](.*?)来源', date_text).group(1).strip().split())

    date_period_text = html.xpath('//div[@class="detail l bk1234"]/h1')[0].xpath('string(.)').strip()
    date_period=re.search(r'(\d+.\d+)-(\d+.\d+)',date_period_text)
    date_period='{}-{}'.format(date_period.group(1),date_period.group(2))
    # print(date_period)

    div_data = html.xpath('//div[@class="art02 mar"]')[0]

    strings = div_data.xpath('string(.)').strip()
    BOPETmoshi_analysis = "".join(re.search(r"BOPET膜市(.*)", strings, re.DOTALL).group(1).strip().split())

    table_rows=div_data.xpath('.//table/tbody/tr')
    if table_rows:
        date_week_begin=table_rows[0].xpath('td[3]')[0].xpath('string(.)').strip()
        date_week_end=table_rows[0].xpath('td[4]')[0].xpath('string(.)').strip()

        product_name = ''
        price_list = {}
        for row in table_rows[1:]:
            td_nums = len(row.xpath('td'))
            if td_nums == 6:
                product_name = row.xpath('td[1]')[0].xpath('string(.)').strip()
                factory = row.xpath('td[2]')[0].xpath('string(.)')
                if re.match("绍兴翔宇",factory):
                    price_week_begin = row.xpath('td[3]')[0].xpath('string(.)').strip()
                    price_week_end = row.xpath('td[4]')[0].xpath('string(.)').strip()
                    change = row.xpath('td[5]')[0].xpath('string(.)').strip()
                    try:
                        remark = row.xpath('td[6]')[0].xpath('string(.)').strip()
                    except:
                        remark = ''
                    row_dict = {
                                date_week_begin: price_week_begin, date_week_end: price_week_end,
                                '涨跌幅': change, '备注': remark
                                }
                    price_list[product_name] = row_dict
                    print(row_dict)
            else:
                factory=row.xpath('td[1]')[0].xpath('string(.)')
                if re.match("绍兴翔宇",factory):
                    price_week_begin = row.xpath('td[2]')[0].xpath('string(.)').strip()
                    price_week_end = row.xpath('td[3]')[0].xpath('string(.)').strip()
                    change = row.xpath('td[4]')[0].xpath('string(.)').strip()
                    try:
                        remark = row.xpath('td[5]')[0].xpath('string(.)').strip()
                    except:
                        remark = ''
                    row_dict = {
                                date_week_begin: price_week_begin, date_week_end: price_week_end,
                                '涨跌幅': change, '备注': remark
                                }
                    price_list[product_name] = row_dict
        print({
            'title':title,
            'date_period':date_period,
                              '绍兴翔宇':price_list,
                              'BOPET_moshi_analysis':BOPETmoshi_analysis})
        try:
            BOPET_week.insert_one({'_id':date,
                              'title':title,
                              'date_period':date_period,
                              '绍兴翔宇':price_list,
                              'BOPET_moshi_analysis':BOPETmoshi_analysis,
                              'spider_time':datetime.now()}
                             )
        except DuplicateKeyError as e:
            print(e)
            print('数据库中已存在该数据')
    else:
        if BOPETmoshi_analysis!='' or BOPETmoshi_analysis!="无" or BOPETmoshi_analysis!="无。":
            try:
                print({
                    'title': title,
                    'date_period': date_period,
                    'BOPET_moshi_analysis': BOPETmoshi_analysis})
                BOPET_week.insert_one({'_id': date,
                                       'title':title,
                                       'date_period': date_period,
                                       'BOPET_moshi_analysis': BOPETmoshi_analysis,
                                       'spider_time': datetime.now()}
                                      )
            except DuplicateKeyError as e:
                print(e)
                print('数据库中已存在该数据')

def parse_PEpage(htmlelement):
    if re.match("区域",htmlelement.xpath('//div[@class="art02 mar"]//table/tbody/tr[1]/td[1]//text()')[0]):
        start=0
    else:
        start=1
    table_attrs=[]
    realfirst_row=htmlelement.xpath('//div[@class="art02 mar"]//table/tbody/tr')[start]
    titletds=realfirst_row.xpath('./td')
    for titletd in titletds:
        table_attr=titletd.xpath('.//text()')[0]
        table_attrs.append(table_attr)
    date_text = htmlelement.xpath('//div[@class="detail l bk1234"]/h1//text()')[0].strip()
    result = re.search(r'(\d{2}\.\d{2}\.\d{2})', date_text)
    if result == None:
        date = table_attrs[6]
        date = date.replace('/','-')
    else:
        date = result.group(1)
        date = '20' + date
        date = date.replace('.', '-')
    #print (date)
    table_rows=htmlelement.xpath('//div[@class="art02 mar"]//table/tbody/tr')[start+1:]
    region=''
    type=''
    factory=''
    for row in table_rows:
        i=3
        item={'发布时间':date}
        td_nums=len(row.xpath("./td"))
        if td_nums==9:
            region=row.xpath('./td[1]//text()')[0]
            type=row.xpath('./td[2]//text()')[0]
            factory=row.xpath('./td[3]//text()')[0]
            cardid=row.xpath('./td[4]//text()')[0]
            if (re.match("LDPE", type) and re.match("上海石化", factory) and re.match("Q281", cardid)) or (re.match("LLDPE", type) and re.match("扬子石化", factory) and re.match("7042", cardid)):
                item[table_attrs[0]] = region
                item[table_attrs[1]] = type
                item[table_attrs[2]] = factory
                item[table_attrs[3]] = cardid
                tds=row.xpath("./td")[4:]
                for td in tds:
                    i+=1
                    if i==5:
                        continue
                    if i==6:
                        item['价格']=td.xpath(".//text()")[0]
                        continue
                    item[table_attrs[i]]=td.xpath(".//text()")[0]
                PE.insert_one(item)
                print(item)
        if td_nums==8:
            type=row.xpath('./td[1]//text()')[0]
            factory=row.xpath('./td[2]//text()')[0]
            cardid=row.xpath('./td[3]//text()')[0]
            if (re.match("LDPE", type) and re.match("上海石化", factory) and re.match("Q281", cardid)) or (re.match("LLDPE", type) and re.match("扬子石化", factory) and re.match("7042", cardid)):
                item[table_attrs[0]] = region
                item[table_attrs[1]] = type
                item[table_attrs[2]] = factory
                item[table_attrs[3]] = cardid
                tds = row.xpath("./td")[3:]
                for td in tds:
                    i += 1
                    if i == 5:
                        continue
                    if i == 6:
                        item['价格'] = td.xpath(".//text()")[0]
                        continue
                    item[table_attrs[i]] = td.xpath(".//text()")[0]
                PE.insert_one(item)
                print(item)
        if td_nums==7:
            factory=row.xpath('./td[1]//text()')[0]
            cardid=row.xpath('./td[2]//text()')[0]
            if (re.match("LDPE", type) and re.match("上海石化", factory) and re.match("Q281", cardid)) or (re.match("LLDPE", type) and re.match("扬子石化", factory) and re.match("7042", cardid)):
                item[table_attrs[0]] = region
                item[table_attrs[1]] = type
                item[table_attrs[2]] = factory
                item[table_attrs[3]] = cardid
                tds = row.xpath("./td")[2:]
                for td in tds:
                    i += 1
                    if i == 5:
                        continue
                    if i == 6:
                        item['价格'] = td.xpath(".//text()")[0]
                        continue
                    item[table_attrs[i]] = td.xpath(".//text()")[0]
                PE.insert_one(item)
                print(item)
        if td_nums==6:
            cardid=row.xpath('./td[1]//text()')[0]
            if (re.match("LDPE", type) and re.match("上海石化", factory) and re.match("Q281", cardid)) or (re.match("LLDPE", type) and re.match("扬子石化", factory) and re.match("7042", cardid)):
                item[table_attrs[0]] = region
                item[table_attrs[1]] = type
                item[table_attrs[2]] = factory
                item[table_attrs[3]] = cardid
                tds = row.xpath("./td")[1:]
                for td in tds:
                    i += 1
                    if i == 5:
                        continue
                    if i == 6:
                        item['价格'] = td.xpath(".//text()")[0]
                        continue
                    item[table_attrs[i]] = td.xpath(".//text()")[0]
                PE.insert_one(item)
                print(item)


def parse_PPDpage(htmlelement):
    date_text = htmlelement.xpath('//div[@class="detail l bk1234"]/h1//text()')[0].strip()
    date = re.search(r'(\d{2}\.\d{2}\.\d{2})', date_text).group(1)
    date = '20' + date
    date = date.replace('.', '-')
    item={'发布时间':date}
    if re.match("生产厂家", htmlelement.xpath('//div[@class="art02 mar"]//table/tbody/tr[1]/td[1]//text()')[0]):
        start = 0
    else:
        start = 1
    table_attrs = []
    realfirst_row = htmlelement.xpath('//div[@class="art02 mar"]//table/tbody/tr')[start]
    titletds = realfirst_row.xpath('./td')
    for titletd in titletds:
        table_attr = check(titletd.xpath('.//text()')[0])
        table_attrs.append(table_attr)
    table_rows=htmlelement.xpath('//div[@class="art02 mar"]//table/tbody/tr')[start+1:]
    for row in table_rows:
        i=-1
        factory=row.xpath('./td[1]//text()')[0]
        cardid=row.xpath('./td[2]//text()')[0]
        if re.match('绍兴三圆',factory) and re.match('T30S',cardid):
            tds=row.xpath('./td')
            for td in tds:
                i+=1
                if i==3:
                    continue
                if i==4:
                    item['价格'] = td.xpath(".//text()")[0]
                    continue
                item[table_attrs[i]]=td.xpath('.//text()')[0]
            if item['价格']=='--':
                continue
            print(item)
            PPD.insert_one(item)



def parse_PPZpage(htmlelement):
    if re.match("中石化", htmlelement.xpath('//div[@class="art02 mar"]//table/tbody/tr[1]/td[1]//text()')[0]):
        start = 0
    else:
        start = 1
    table_attrs = []
    realfirst_row = htmlelement.xpath('//div[@class="art02 mar"]//table/tbody/tr')[start]
    titletds = realfirst_row.xpath('./td')
    for titletd in titletds:
        table_attr = check(titletd.xpath('.//text()')[0])
        table_attrs.append(table_attr)
    date_text = htmlelement.xpath('//div[@class="detail l bk1234"]/h1//text()')[0].strip()
    result = re.search(r'(\d{2}\.\d{2}\.\d{2})', date_text)
    if result==None:
        date=table_attrs[5]
        date = '20' + date
        date = date.replace('.', '-')
        date = date.replace('/','-')
    else:
        date=result.group(1)
        date = '20' + date
        date = date.replace('.', '-')
    table_rows = htmlelement.xpath('//div[@class="art02 mar"]//table/tbody/tr')[start + 1:]
    zhongshihua= ''
    factory = ''
    for row in table_rows:
        i = 2
        item = {'发布时间': date}
        td_nums = len(row.xpath("./td"))
        #print(td_nums)
        if td_nums ==8:
            zhongshihua = row.xpath('./td[1]//text()')[0]
            factory = row.xpath('./td[2]//text()')[0]
            cardid = row.xpath('./td[3]//text()')[0]
            if (re.match("上海石化", factory) and re.match("F280/F280S", cardid)) or (re.match("镇海炼化", factory) and re.match("T30S", cardid)):
                item[table_attrs[0]] = zhongshihua
                item[table_attrs[1]] = factory
                item[table_attrs[2]] = cardid
                tds = row.xpath("./td")[3:]
                for td in tds:
                    i+=1
                    if i==4:
                        continue
                    if i==5:
                        item['价格'] = td.xpath(".//text()")[0]
                        continue
                    item[table_attrs[i]] = td.xpath(".//text()")[0]
                PPZ.insert_one(item)
                print(item)
        if td_nums == 7:
            factory = row.xpath('./td[1]//text()')[0]
            cardid = row.xpath('./td[2]//text()')[0]
            if (re.match("上海石化", factory) and re.match("F280/F280S", cardid)) or (
                    re.match("镇海炼化", factory) and re.match("T30S", cardid)):
                item[table_attrs[0]] = zhongshihua
                item[table_attrs[1]] = factory
                item[table_attrs[2]] = cardid
                tds = row.xpath("./td")[2:]
                for td in tds:
                    i += 1
                    if i == 4:
                        continue
                    if i == 5:
                        item['价格'] = td.xpath(".//text()")[0]
                        continue
                    item[table_attrs[i]] = td.xpath(".//text()")[0]
                PPZ.insert_one(item)
                print(item)
        if td_nums == 6:
            cardid = row.xpath('./td[1]//text()')[0]
            if (re.match("上海石化", factory) and re.match("F280/F280S", cardid)) or (
                    re.match("镇海炼化", factory) and re.match("T30S", cardid)):
                item[table_attrs[0]] = zhongshihua
                item[table_attrs[1]] = factory
                item[table_attrs[2]] = cardid
                tds = row.xpath("./td")[1:]
                for td in tds:
                    i += 1
                    if i == 4:
                        continue
                    if i == 5:
                        item['价格'] = td.xpath(".//text()")[0]
                        continue
                    item[table_attrs[i]] = td.xpath(".//text()")[0]
                PPZ.insert_one(item)
                print(item)

def check(str):
    if str.find('.')!=-1:
        str=str.replace('.','-')
        return str
    return str

"""
mongo DB
"""
client=MongoClient('localhost',27017)
database=client['project']
BOPP_day=database['BOPP_day']
CPP_day=database['CPP_day']
PPD = database['PPD']
PPZ = database['PPZ']
PE = database['PE']
BOPET_day=database['BOPET_day']
BOPET_week=database['BOPET_week']

