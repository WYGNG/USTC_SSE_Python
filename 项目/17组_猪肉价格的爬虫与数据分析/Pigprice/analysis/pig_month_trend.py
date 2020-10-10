import sys
sys.path.append("./")
from spider.request_factory import bot, urls, get_input
from bs4 import BeautifulSoup
from urllib import parse
from pprint import pprint
import json
import pandas as pd
import matplotlib.pyplot as plt
category = ['外三元', '内三元', '土杂猪', '玉米', '豆粕']
cities = ['北京市', '上海市', '天津市', '重庆市', '广东省', '福建省', '浙江省', '江苏省', '山东省', '辽宁省', '江西省', '四川省', '陕西省', '湖北省', '河南省', '河北省', '山西省', '内蒙古']

res = bot.get(url=urls.get('trend'))
bs = BeautifulSoup(res.text, "html.parser")
provinces = bs.select("#pri_province")[0].text.strip('\n').replace("更多\n", "").split('\n')
dateType = {
    'month': 30,
    'year': 365
}
# days = get_input(dateType, 'dateType')
days = 'month'

items = {}
for item in bs.select(".charts_type > div"):
    items[item.text] = item.attrs.get('value')

# province = get_input(provinces, 'province')
province = cities[0]

# item = get_input(items, 'item')
item = category[0]
res = bot.get(urls.get('trend_data').format(province=parse.quote(province.encode('gbk')), days=dateType.get(days),
                                            pid=item),
              )

a = json.loads(res.text)
pprint(a)

# df1 = pd.DataFrame([[a["name"]]+eval(a["all"]),[a["name"]]+eval(a["province"])],
#                     index = [a["yyear"],a["year"]],
#                     columns = ["省份"]+eval(a["day"]))
null = None                    
df1 = pd.DataFrame([eval(a["all"])[:-1],eval(a["province"])[:-1]],
                    index = [a["yyear"],a["year"]],
                    columns = eval(a["day"])[:-1])
df1 = df1.transpose()
# plt.figure()
# plt.subplot(221)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig, axes = plt.subplots(2, 2, figsize=(50, 50))
df1.plot(ax = axes[0][0],kind = 'line',title=a["name"])
# plt.show()
##########################################
province = cities[1]

item = category[0]
res = bot.get(urls.get('trend_data').format(province=parse.quote(province.encode('gbk')), days=dateType.get(days),
                                            pid=item),
              )

b = json.loads(res.text)
pprint(b)
df2 = pd.DataFrame([eval(b["all"])[:-1],eval(b["province"])[:-1]],
                    index = [b["yyear"],b["year"]],
                    columns = eval(b["day"])[:-1])
df2 = df2.transpose()
# plt.subplot(222)
df2.plot(ax = axes[0][1],kind = 'line',title=b["name"])
# plt.show()
##############################################
province = cities[4]

item = category[0]
res = bot.get(urls.get('trend_data').format(province=parse.quote(province.encode('gbk')), days=dateType.get(days),
                                            pid=item),
              )

c = json.loads(res.text)
pprint(c)
df3 = pd.DataFrame([eval(c["all"])[:-1],eval(c["province"])[:-1]],
                    index = [c["yyear"],c["year"]],
                    columns = eval(c["day"])[:-1])
df3 = df3.transpose()
# plt.subplot(223)
df3.plot(ax = axes[1][0],kind = 'line',title=c["name"])
# plt.show()
##############################################
province = cities[11]

item = category[0]
res = bot.get(urls.get('trend_data').format(province=parse.quote(province.encode('gbk')), days=dateType.get(days),
                                            pid=item),
              )
d = json.loads(res.text)
pprint(d)
df4 = pd.DataFrame([eval(d["all"])[:-1],eval(d["province"])[:-1]],
                    index = [d["yyear"],d["year"]],
                    columns = eval(d["day"])[:-1])
df4 = df4.transpose()
# plt.subplot(223)
df4.plot(ax = axes[1][1],kind = 'line',title=d["name"])
# plt.show()
############北京上海广东2018对比
# df1x = df1.drop(['2019'],axis=1)
# df1x.rename(columns={2018:a['name']},inplace=True)
# df2x = df2.drop(['2019'],axis=1)
# df2x.rename(columns={2018:b['name']},inplace=True)
# df3x = df3.drop(['2019'],axis=1)
# df3x.rename(columns={2018:c['name']},inplace=True)
# df4x = df4.drop(['2019'],axis=1)
# df4x.rename(columns={2018:d['name']},inplace=True)
# res = pd.concat([df1x,df2x,df3x,df4x],axis=1)
# # res.index = ['2018.1','2018.2','2018.3','2018.4','2018.5','2018.6','2018.7','2018.8','2018.9','2018.10','2018.11','2018.12']
# ############北京上海广东2019对比
# df1x = df1.drop([2018],axis=1)
# df1x.rename(columns={'2019':a['name']},inplace=True)
# df2x = df2.drop([2018],axis=1)
# df2x.rename(columns={'2019':b['name']},inplace=True)
# df3x = df3.drop([2018],axis=1)
# df3x.rename(columns={'2019':c['name']},inplace=True)
# df4x = df4.drop([2018],axis=1)
# df4x.rename(columns={'2019':d['name']},inplace=True)
# res2 = pd.concat([df1x,df2x,df3x,df4x],axis=1)
# # res2.index = ['2019.1','2019.2','2019.3','2019.4','2019.5','2019.6','2019.7','2019.8','2019.9','2019.10','2019.11','2019.12']
# # plt.subplot(224)
# res2 = pd.concat([res,res2],axis = 0)
# res2.plot(kind = 'bar',title='18-19价格对比',figsize=(50,25))
plt.show()