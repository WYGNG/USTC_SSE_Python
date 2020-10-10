# coding=UTF-8
from spider.request_factory import bot, urls, load_html_to_bs
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib import parse
from pprint import pprint
import json
from spider.tools import countTime


@countTime
def get_trend_data():
    res = {}
    bs = load_html_to_bs(urls.get('trend'))
    provinces = bs.select("#pri_province")[0].text.strip('\n').replace("更多\n", "").split('\n')
    items = {}
    for item in bs.select(".charts_type > div"):
        items[item.text] = item.attrs.get('value')
    dateType = {
        'month': 30,
        'year': 365
    }

    for date in dateType:
        for province in provinces:
            for k, v in items.items():
                date, province, k, result = _get_data(date, dateType, province, k, v)
                if not res.get(date):
                    res[date] = {}
                if not res[date].get(province):
                    res[date][province] = {}
                res[date][province][k] = result
    return res, 'trend'


@countTime
def get_trend_data_concurrent():
    res = {}
    bs = load_html_to_bs(urls.get('trend'))
    provinces = bs.select("#pri_province")[0].text.strip('\n').replace("更多\n", "").split('\n')
    items = {}
    for item in bs.select(".charts_type > div"):
        items[item.text] = item.attrs.get('value')
    dateType = {
        'month': 30,
        'year': 365
    }
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for date in dateType:
            for province in provinces:
                for k, v in items.items():
                    futures.append(executor.submit(_get_data, date, dateType, province, k, v))
        for future in as_completed(futures):
            date, province, k, result = future.result()
            if not res.get(date):
                res[date] = {}
            if not res[date].get(province):
                res[date][province] = {}
            res[date][province][k] = result
    return res, 'trend'


def _get_data(date, dateType, province, k, v):
    print("crawling {} {} {}".format(date, province, k))
    res = bot.get(urls.get('trend_data').format(province=parse.quote(province.encode('gbk')), days=dateType.get(date),
                                                pid=v),
                  )

    return date, province, k, json.loads(res.text)


if __name__ == '__main__':
    pprint(get_trend_data_concurrent())
