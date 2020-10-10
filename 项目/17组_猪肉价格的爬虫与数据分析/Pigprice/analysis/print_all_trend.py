import sys
sys.path.append("./")
from matplotlib import pyplot as plt
from pandas import DataFrame
from spider.request_factory import get_data_by_item_name

category = ['外三元', '内三元', '土杂猪', '玉米', '豆粕']
cities = ['北京市', '上海市', '天津市', '重庆市', '广东省', '福建省', '浙江省', '江苏省', '山东省', '辽宁省', '江西省', '四川省', '陕西省', '湖北省', '河南省', '河北省', '山西省', '内蒙古']

# 大豆
df_data_bean_price = DataFrame()
for i in range(18):
    temp2 = get_data_by_item_name('bean', cities[i])
    df_temp2 = DataFrame(temp2[1: ], columns=temp2[0])
    df_temp2['cities'] = cities[i]
    df_data_bean_price = df_data_bean_price.append(df_temp2, ignore_index=True)
del df_data_bean_price['地区']
del df_data_bean_price['品种']
del df_data_bean_price['分类']
df_data_bean_price['价格'] = df_data_bean_price['价格'].apply(float)
df_data_bean_price = df_data_bean_price.groupby(['日期'])[['价格']].mean()/100
df_data_bean_price = df_data_bean_price.reset_index()
df_data_bean_price = df_data_bean_price.sort_values(by='日期')
df_data_bean_price.rename(columns={'价格': '豆粕'}, inplace=True)


# 玉米
df_data_corn_price = DataFrame()
for i in range(18):
    temp3 = get_data_by_item_name('corn', cities[i])
    df_temp3 = DataFrame(temp3[1: ], columns=temp3[0])
    df_temp3['cities'] = cities[i]
    df_data_corn_price = df_data_corn_price.append(df_temp3, ignore_index=True)
del df_data_corn_price['地区']
del df_data_corn_price['品种']
del df_data_corn_price['分类']
df_data_corn_price['价格'] = df_data_corn_price['价格'].apply(float)
df_data_corn_price_ = df_data_corn_price.groupby(['日期'])[['价格']].mean()/100
df_data_corn_price = df_data_corn_price_.reset_index()
df_data_corn_price = df_data_corn_price.sort_values(by='日期')
df_data_corn_price.rename(columns={'价格': '玉米'}, inplace=True)

# 猪肉
df_data_baby_data = DataFrame()
for i in range(18):
    temp1 = get_data_by_item_name('baby_data', cities[i])
    df_temp1 = DataFrame(temp1[1: ], columns=temp1[0])
    df_data_baby_data = df_data_baby_data.append(df_temp1, ignore_index=True)
del df_data_baby_data['地区']
del df_data_baby_data['品种']
del df_data_baby_data['分类']
df_data_baby_data['价格'] = df_data_baby_data['价格'].apply(float)
df_data_baby_data = df_data_baby_data.groupby(['日期'])[['价格']].mean()
df_data_baby_data = df_data_corn_price_ * 2
df_data_baby_data = df_data_baby_data.reset_index()
df_data_baby_data = df_data_baby_data.sort_values(by='日期')
df_data_baby_data.rename(columns={'价格': '猪肉'}, inplace=True)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig,axes = plt.subplots(1)
df_data_corn_price.plot(ax=axes, kind='line', x='日期', color='green', title='全国价格走势图')
df_data_baby_data.plot(ax=axes, x='日期', kind='line', color='red')
df_data_bean_price.plot(ax=axes, kind='line', x='日期', color='blue')

# 猪肉        元/kg
# 豆粕 玉米   元/10kg
plt.show()