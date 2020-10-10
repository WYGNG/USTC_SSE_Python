#收集多个城市的气象数据，然后利用定时任务 每小时各收集一份
#共24h*10 240文件
#命名规则是{城市名}_{小时}.json

#coding:utf-8
import time
import json
import os

import urllib.request

#准备时间数据
total_secs = int(time.time())
cur_secs = total_secs % 60
total_mins = total_secs // 60
cur_mins = total_mins % 60
total_hours = total_mins // 60
cur_hours = total_hours % 24
chinatime = (cur_hours + 8) % 24

curtime = str(chinatime) if len(str(chinatime)) == 2 else '0'+str(chinatime)

cities = [('suzhou', 1886760),
          ('shanghai', 1796236),
          ('hangzhou', 1808926),
          ('jiaxing', 1805953),
          ('wuxi', 1790923),
          ('taizhou', 1793505),
          ('changzhou', 1815456),
          ('nanjing', 1799962),
          ('wuhu', 7069199),
          ('nantong', 1799722)]

for i in range(len(cities)):
    url = "https://api.openweathermap.org/data/2.5/weather?id=%d" \
          "&appid=896a0c8446b4812422173d0c5fe36194" % cities[i][1]
    resp = urllib.request.urlopen(url)
    data = json.loads(resp.read().decode())
    dir = r'D:\feiwu\data'
    path = os.path.join(dir, cities[i][0] + curtime + '.json')
    with open(path, 'w') as file:
        file.write(json.dumps(data, indent=2))