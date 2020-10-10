
# coding: utf-8

from spider.request_factory import get_data_by_item_name
import numpy as np

data = get_data_by_item_name('bean')

import matplotlib


#转成array才能画图么
data=np.array(data)


import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties
#font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

plt.rcParams['font.sans-serif']=['FangSong'] #用来正常显示中文标签
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'


#尝试添加中文城市横坐标标签
label_list=data[1:,1]
label_list

#纵坐标数据集
num_list=data[1:,4]

#数据都是numpy.str_型的，笨比方法转成float，待改进
list_len=num_list.size
num_flist=[]
for i in range(list_len):
    num_flist.append(float(num_list[i]))


#绘制条形图
x = range(len(num_list))
rects1 = plt.bar(left=x, height=num_flist, width=0.4, alpha=0.8, color='red', label=u"henan")
ymax=max(data[1:,4])
plt.ylim(0,float(ymax))
plt.ylabel("price")

#设置x轴刻度
plt.xticks([index + 0.2 for index in x], label_list)
plt.xlabel("city")
plt.title(u"河南")
plt.legend()


#设置rect高度文本
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")


plt.show()




