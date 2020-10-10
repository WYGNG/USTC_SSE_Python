import sys
sys.path.append("./")
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from pandas import Series, DataFrame
from spider.request_factory import get_data_by_item_name

# category = ['外三元', '内三元', '土杂猪', '玉米', '豆粕']
cities = ['北京市', '上海市', '天津市', '重庆市', '广东省', '福建省', '浙江省', '江苏省', '山东省', '辽宁省', '江西省', '四川省', '陕西省', '湖北省', '河南省', '河北省', '山西省', '内蒙古']


# 取出所有猪肉价格的信息
df_data = DataFrame()
for i in range(18):
    temp = get_data_by_item_name('baby_data', cities[i])
    df_temp = DataFrame(temp[1: ], columns=temp[0])
    df_temp['cities'] = cities[i]
    df_data = df_data.append(df_temp, ignore_index=True)

# 对每列数据进行处理
df_data.rename(columns={'日期': 'date'}, inplace=True)
df_data.rename(columns={'地区': 'area'}, inplace=True)
del df_data['品种']
df_data.rename(columns={'分类': 'category'}, inplace=True)
df_data.rename(columns={'价格': 'price'}, inplace=True)
df_data['price'] = df_data['price'].apply(float)

# 解决显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 猪仔一个省没有重复的
# df_data_sub = df_data.drop_duplicates(['date', 'cities', 'category'], inplace=True)




'''
fig = plt.plot()
df_data = df_data.groupby(['date']).mean()
df_data.plot()
'''

fig, axes = plt.subplots(9, 2, figsize=(12, 50))
num = 0
for city in cities:
    df_data_print = df_data.loc[df_data['cities'] == city]
    n = num % 2
    m = num // 2
    # df_data_print = df_data_print.drop_duplicates(['date'])
    df_data_print.sort_index(by='date')
    df_data_print.plot(ax=axes[m, n], y='price', yticks=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45], title=cities[num])
    num = num + 1


'''
数据太少，每个省没有按猪肉的种类画走势
for city in cities:
    df_data_print = df_data.loc[df_data['cities'] == city]
    class_info = df_data_print['category'].unique()
    for temp_class in class_info:
        temp_data = df_data_print[df_data_print['category'].isin([temp_class])]
        n = num % 2
        m = num // 2
        temp_data = temp_data.sort_index(by='date')
        temp_data = temp_data.drop_duplicates(['date', 'cities'])
        temp_data.plot(ax=axes[m, n], x='date', y='price')
    num = num + 1
'''
plt.show()





