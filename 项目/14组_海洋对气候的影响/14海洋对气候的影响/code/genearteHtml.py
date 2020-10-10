from pyecharts.charts import Geo
import pandas as pd
from pyecharts import options as opts
datafile = r'D:\feiwu\test.csv'
data = pd.read_csv(datafile)
city  = data['city'] #获取名字为flow列的数据
city_list = city.values.tolist()#将csv文件中flow列中的数据保存到列表中

temp  = data['temp'] #获取名字为flow列的数据
temp_list = temp.values.tolist()#将csv文件中flow列中的数据保存到列表中

c = ( Geo()
.add_schema(maptype="china")
 .add("温度", [list(z) for z in zip(city_list, temp_list)])
.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=30), title_opts=opts.TitleOpts(title="全国部分城市十一月平均最高气温数据分布"),
 )
)
c.render()