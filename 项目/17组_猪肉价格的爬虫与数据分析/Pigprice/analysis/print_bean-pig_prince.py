import sys
sys.path.append("./")
from spider.request_factory import bot, urls, get_input
from bs4 import BeautifulSoup
from urllib import parse
from pprint import pprint
import json
import pandas as pd
import matplotlib.pyplot as plt
#category = ['外三元', '内三元', '土杂猪', '玉米', '豆粕','白条肉']
category = ['19', '22', '20', '8', '9','10']
cities = ['北京市', '上海市', '天津市', '重庆市', '广东省', '福建省', '浙江省', '江苏省', '山东省', '辽宁省', '江西省', '四川省', '陕西省', '湖北省', '河南省', '河北省', '山西省', '内蒙古']

res = bot.get(url=urls.get('trend'))
bs = BeautifulSoup(res.text, "html.parser")
provinces = bs.select("#pri_province")[0].text.strip('\n').replace("更多\n", "").split('\n')

dateType = {
    'month': 30,
    'year': 365
}

days = 'year'

province = cities[0]

#item = category[0]
res1 = bot.get(urls.get('trend_data').format(province=parse.quote(province.encode('gbk')), days=dateType.get(days),
                                            pid=category[0]),
              )

res2 = bot.get(urls.get('trend_data').format(province=parse.quote(province.encode('gbk')), days=dateType.get(days),
                                            pid=category[3]),
              )
              
res3 = bot.get(urls.get('trend_data').format(province=parse.quote(province.encode('gbk')), days=dateType.get(days),
                                            pid=category[4]),
              )

a = json.loads(res1.text)
pprint(a)
b=json.loads(res2.text)
pprint(b)
c=json.loads(res3.text)

df1 = pd.DataFrame([eval(a["province"])],
                    index = [a["year"]],
                    columns = [1,2,3,4,5,6,7,8,9,10,11])
df1 = df1.transpose()



b2=[i/100 for i in eval(b["province"])]	

df2 = pd.DataFrame([b2],
                    index = [b["year"]],
                    columns = [1,2,3,4,5,6,7,8,9,10,11])
df2 = df2.transpose()

b3=[i/100 for i in eval(c["province"])]	

df3 = pd.DataFrame([b3],
                    index = [c["year"]],
                    columns = [1,2,3,4,5,6,7,8,9,10,11])
df3 = df3.transpose()


print(df1)
print(df2)
print(df3)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(df1,'b-o',label='外三元')
plt.plot(df2,'r-o',label='玉米')
plt.plot(df3,'y-o',label='豆粕')
plt.legend()
plt.show()





