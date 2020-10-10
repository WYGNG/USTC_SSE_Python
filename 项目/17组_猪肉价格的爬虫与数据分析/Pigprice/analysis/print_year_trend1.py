import sys
sys.path.append("./")
from spider.request_factory import bot, urls, get_input
from bs4 import BeautifulSoup
from urllib import parse
from pprint import pprint
import json
import pandas as pd
from matplotlib import pyplot as plt
category = ['外三元', '内三元', '土杂猪', '玉米', '豆粕']
cities = ['北京市', '上海市', '天津市', '重庆市', '广东省', '福建省', '浙江省', '江苏省', '山东省', '辽宁省', '江西省', '四川省', '陕西省', '湖北省', '河南省', '河北省', '山西省', '内蒙古']

res = bot.get(url=urls.get('trend'))
bs = BeautifulSoup(res.text, "html.parser")
provinces = bs.select("#pri_province")[0].text.strip('\n').replace("更多\n", "").split('\n')
dateType = {
    'month': 30,
    'year': 365
}
days = get_input(dateType, 'year')

items = {}
for item in bs.select(".charts_type > div"):
    items[item.text] = item.attrs.get('value')

province = get_input(provinces, '全国')

item = get_input(items, '外三元')
res = bot.get(urls.get('trend_data').format(province=parse.quote(province.encode('gbk')), days=dateType.get(days),
                                            pid=item),
              )

a = json.loads(res.text)
# pprint(a)

df1 = pd.DataFrame([[a["name"]]+eval(a["all"]),[a["name"]]+eval(a["province"])],
                    index = [a["yyear"],a["year"]],
                    columns = ["省份"]+eval(a["day"]))

df = df1.transpose()
df = df[1:]
df.reset_index(drop=True)
df[2018].apply(float)
df['2019'].apply(float)
df['2019'][11] = 35

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig,axes = plt.subplots(1)
df.plot()
plt.show()

