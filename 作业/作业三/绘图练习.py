# 导入绘图模块
import matplotlib.pyplot as plt
# 构建数据
price = [39.5,39.9,45.4,38.9,33.34]

# 中文乱码的处理
plt.rcParams['font.sans-serif'] =["KaiTi"]
plt.rcParams['axes.unicode_minus'] = False

# 绘图
plt.barh(range(5), price, align = 'center',color='steelblue', alpha = 0.8)
# 添加轴标签
plt.xlabel('价格')
# 添加标题
plt.title('不同平台书的最低价比较')
# 添加刻度标签
plt.yticks(range(5),['亚马逊','当当网','中国图书网','京东','天猫'])
# 设置Y轴的刻度范围
plt.xlim([32,47])

# 为每个条形图添加数值标签
for x,y in enumerate(price):
    plt.text(y+0.1,x,'%s' %y,va='center')
# 显示图形    
plt.show()