import sys
sys.path.append("./")
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from spider.request_factory import load_html_to_bs, urls, get_input
import re

category = ['外三元', '内三元', '土杂猪', '玉米', '豆粕']

items = {}
for i in load_html_to_bs(urls.get('rank_index')).select(".list_nav div a"):
    items[i.text] = i.attrs['href']

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig, axes = plt.subplots(5, 1, figsize=(12, 50))
num = 0
for cg in category:
    item = get_input(items, 'item', cg)
    a = load_html_to_bs(urls.get('baseUrl') + items.get(item)).select(".list_tab ")
    result = [re.split('\n| ',i) for i in a[0].text.strip('\n\n').split('\n\n\n')]
    df = pd.DataFrame(result[1:],columns = result[0])
    df['11-13'] = df['11-13'].apply(float)
    df['11-12'] = df['11-12'].apply(float)
    df['排名'] = df['排名'].apply(float)
    df = df.sort_values(by='排名', ascending=False)
    df['排名'] = df['排名'].apply(str)
    df.plot(ax=axes[num], kind='barh',x='省市',title=cg)
    num = num + 1

plt.show()




