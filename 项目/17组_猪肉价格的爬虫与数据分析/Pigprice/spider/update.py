# coding=UTF-8
from spider.request_factory import get_all_data_by_name_concurrent
from spider.price_trend_c import get_trend_data
from spider.pig_rank import get_pig_rank
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

if __name__ == '__main__':
    items = ['corn', 'bean', 'baby']
    json_data = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(get_all_data_by_name_concurrent, i) for i in items]
        futures.append(executor.submit(get_pig_rank, ))
        futures.append(executor.submit(get_trend_data, ))
    for f in as_completed(futures):
        data, name = f.result()
        json_data[name] = data

    with open('data.json', 'w') as fs:
        fs.write(json.dumps(json_data, indent=2, ensure_ascii=False))
