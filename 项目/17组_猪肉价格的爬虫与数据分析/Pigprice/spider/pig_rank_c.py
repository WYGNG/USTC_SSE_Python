# coding=UTF-8


from spider.request_factory import load_html_to_bs, urls
from pprint import pprint
import re
from concurrent.futures import ThreadPoolExecutor, as_completed


def _get_rank_by_item(item_name, url):
    print("crawling {} rank".format(item_name))
    a = load_html_to_bs(urls.get('baseUrl') + url).select(".list_tab ")
    result = [re.split('\n| ', i) for i in a[0].text.strip('\n\n').split('\n\n\n')]
    return item_name, result


def get_pig_rank():
    aaa = {}
    items = {}
    for i in load_html_to_bs(urls.get('rank_index')).select(".list_nav div a"):
        items[i.text] = i.attrs['href']
    # item = get_input(items, 'item')

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(_get_rank_by_item, k, v) for k, v in items.items()]
    for future in as_completed(futures):
        item, res = future.result()
        aaa[item] = res
    return aaa, 'rank'


if __name__ == '__main__':
    pprint(get_pig_rank())
