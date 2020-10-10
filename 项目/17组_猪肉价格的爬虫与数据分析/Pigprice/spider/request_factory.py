import requests
from bs4 import BeautifulSoup
import re
import json
from spider.tools import countTime
from concurrent.futures import ThreadPoolExecutor,as_completed


urls = {
    "trend": r"https://bj.zhue.com.cn/mobi/zoushi.php",
    "trend_data": r"https://bj.zhue.com.cn/mobi/zoushi.php?act=pricecure&province_name={province}&day={days}&puote_small_id={pid})",
    "baby_data": r"https://bj.zhue.com.cn/mobi/list.php?",
    "baby": r"https://bj.zhue.com.cn/mobi/list.php?sort=1",
    "corn": r"https://bj.zhue.com.cn/mobi/list.php?s_id=8",
    "bean": r"https://bj.zhue.com.cn/mobi/list.php?s_id=9",
    "rank_index": r"https://bj.zhue.com.cn/mobi/mpriceph.php?act=list&typeid=19",
    "baseUrl": r"https://bj.zhue.com.cn/mobi/"
}
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "acw_tc=7b39758215731168447986505ead688fcae474967124ef8ded09cfeac5feb3; QbnN_c9af_saltkey=vU91ugI3; QbnN_c9af_lastvisit=1573113245; __51cke__=; QbnN_c9af_lastact=1573274055%09api.php%09zypic; __tins__19698563=%7B%22sid%22%3A%201573273893386%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201573275855654%7D; __tins__19698571=%7B%22sid%22%3A%201573273893390%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201573275855661%7D; __51laig__=4; top_ad_close=1",
    "Host": "bj.zhue.com.cn",
    "Referer": "https//bj.zhue.com.cn/mobi/",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
}

bot = requests.session()
bot.headers = header


def load_html_to_bs(url):
    return BeautifulSoup(bot.get(url).text, 'html.parser')


def get_data_by_item_name(item, input_city):
    html = BeautifulSoup(bot.get(urls.get(item)).text, 'html.parser')
    baseUrl = urls.get('baseUrl')
    dataUrl = urls.get('baby_data')

    cities = {}
    for city in html.select(".pri_province > a "):
        cities[city.text.strip()] = city.attrs['href']
    city_name = input_city
    for city in html.select(".pri_province > a "):
        cities[city.text.strip()] = city.attrs['href']
    res = (bot.get(baseUrl + cities.get(city_name)))
    r = r"(?<=list.php\?).+?(?=\')"
    p = re.compile(r)
    cid = re.search(p, res.text)
    data = json.loads(bot.get(dataUrl + cid.group()).text)
    result = [BeautifulSoup(res.text, 'html.parser').select('.pri_type')[0].text.strip().split('\n')]
    for d in data:
        result.append([i.text for i in BeautifulSoup(d.get("pro-inner"), 'html.parser').select("li")])

    return result


def get_input(items, name):
    print(items if type(items) == list else items.keys())
    while 1:
        print('input {}:'.format(name))
        item = input()
        if item in items if type(items) == list else items.get(item):
            return item
        else:
            print('{} not exist'.format(item))


@countTime
def get_all_data_by_name(item):
    aaa = {}
    html = BeautifulSoup(bot.get(urls.get(item)).text, 'html.parser')
    baseUrl = urls.get('baseUrl')
    dataUrl = urls.get('baby_data')

    cities = {}
    for city in html.select(".pri_province > a "):
        cities[city.text.strip()] = city.attrs['href']
    for city_name in cities.keys():
        print("crawling {}...".format(city_name))
        res = (bot.get(baseUrl + cities.get(city_name)))
        r = r"(?<=list.php\?).+?(?=\')"
        p = re.compile(r)
        cid = re.search(p, res.text)
        data = json.loads(bot.get(dataUrl + cid.group()).text)
        result = [BeautifulSoup(res.text, 'html.parser').select('.pri_type')[0].text.strip().split('\n')]
        for d in data:
            result.append([i.text for i in BeautifulSoup(d.get("pro-inner"), 'html.parser').select("li")])
        aaa[city_name] = result

    return aaa


@countTime
def get_all_data_by_name_concurrent(item):
    aaa = {}
    html = BeautifulSoup(bot.get(urls.get(item)).text, 'html.parser')
    cities = {}
    for city in html.select(".pri_province > a "):
        cities[city.text.strip()] = city.attrs['href']

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(_get_data_by_city_id, city_name, cities[city_name]) for city_name in cities.keys()]
    for future in as_completed(futures):
        name, res = future.result()
        aaa[name] = res
    return aaa, item


def _get_data_by_city_id(city_name, city_id):
    baseUrl = urls.get('baseUrl')
    dataUrl = urls.get('baby_data')
    print("crawling {}...".format(city_name))
    res = (bot.get(baseUrl + city_id))
    r = r"(?<=list.php\?).+?(?=\')"
    p = re.compile(r)
    cid = re.search(p, res.text)
    data = json.loads(bot.get(dataUrl + cid.group()).text)
    result = [BeautifulSoup(res.text, 'html.parser').select('.pri_type')[0].text.strip().split('\n')]
    for d in data:
        result.append([i.text for i in BeautifulSoup(d.get("pro-inner"), 'html.parser').select("li")])
    return city_name, result