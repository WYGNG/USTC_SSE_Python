import requests
import pandas as pd
import re

# 构造请求头


headers = {"User-Agent": "Mozilla/5.0"}

cities = {
          'shanghai':58362,
          'hangzhou':58457,
          'nanjing':58238,
          'hefei':58321,
          'fuzhou':58847,
          'nanchang':58606,
          'wuhan':57494,
          'changsha':57687,
          'chongqing':57516,
          'chengdu':56294,
          'taiyuan':53772,
          'shijiazhuang':53698,
          'nanning':59431,
          'taibei':71294,
          'lanzhou':52889,
          'guangzhou':59287,
          'jinan':54823,
          'zhenzhou':57083,
          'guiyang':57816,
          'xian':57036,
          'lasa':55591,
          'beiing':54511,
          'tianjin':54527,
          'haikou':59758,
          'xianggang':45007,
          'aomen':45011

}
# 'kunming':56778,
# 生成所有需要抓取的链接

year = 2017
month = 11
urls = []
for city, num in cities.items():
    urls.append('http://tianqi.2345.com/t/wea_history/js/%s_%s%s.js' % (num, year, month))

keys = ['city', 'temp']
j = 0
frames = []
for url in urls:
    info = []
    response = requests.get(url, headers=headers).text
    high = re.findall("bWendu:'(.*?)',", response)
    high = [eval(x[:-1]) for x in high]
    print(high)
    city = re.findall("city:'(.*?)',", response)
    info += city

    sum = 0.0
    for i in range(len(high)):
        sum += high[i]
    avg_high = round(sum / len(high),2)
    info.append(avg_high)

    dict1 = dict(zip(keys, info))
    df = pd.DataFrame(dict1, index=[j])
    frames.append(df)
    j += 1

result = pd.concat(frames)
result.to_csv('generateThermodynamicChart.csv')