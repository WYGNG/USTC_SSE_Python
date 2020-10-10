import pymongo
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import re

plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.project
PPZ_data=db.PPZ

def get_PPZ_data(use):
    results = PPZ_data.find({'用途':use}).sort("发布时间", pymongo.DESCENDING)
    factory =results[0]['厂家']
    count = results.count()
    price = []
    date = []
    for i in range(count - 1, -1, -1):
        price.append(int(results[i]['价格']))
        date.append(results[i]['发布时间'])
    plt.figure(figsize=(13, 8))
    plt.plot(date, price, linewidth=2, color='blue', label=factory+use)
    plt.legend()
    plt.title("国内中石化PP出厂"+factory+use+"价格折线图", fontsize=14)
    plt.xlabel("发布时间（年/月/日）", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.yaxis.set_major_locator(MultipleLocator(100))
    plt.tick_params(axis='both')
    filename = "国内中石化PP出厂"+factory+use+"价格折线图.png"
    plt.savefig(filename)
    plt.show()
    return filename

def get_PPZ_data_week():
    results1 = PPZ_data.find({'厂家':'上海石化'}).sort("发布时间", pymongo.DESCENDING).limit(7)
    results2 = PPZ_data.find({'厂家':'镇海炼化'}).sort("发布时间", pymongo.DESCENDING).limit(7)
    count = results1.count()
    s_price = []
    z_price = []
    date = []
    for i in range(6, -1, -1):
        s_price.append(int(results1[i]['价格']))
        z_price.append(int(results2[i]['价格']))
        date.append(results1[i]['发布时间'])
    plt.figure(figsize=(10, 8))
    plt.plot(date, s_price, linewidth=2, color='blue', label="上海石化BOPP膜料")
    plt.plot(date, z_price, linewidth=2, color='red', label="镇海炼化拉丝")
    plt.legend()
    plt.title("国内中石化PP出厂价格(最近一周）折线图", fontsize=14)
    plt.xlabel("发布时间（年/月/日）", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    plt.tick_params(axis='both')
    filename = "国内中石化PP出厂价格（最近一周）折线图.png"
    plt.savefig(filename)
    plt.show()
    return filename

def get_table_PPZSH():
    results1 =PPZ_data.find({'厂家':'上海石化'}).sort("发布时间", pymongo.DESCENDING).limit(5)
    results2 = PPZ_data.find({'厂家': '镇海炼化'}).sort("发布时间", pymongo.DESCENDING).limit(5)
    statistics_price1 = []
    statistics_price2 = []
    for i in range(5):
        statistics_price1.append(results1[i].get("价格"))
        statistics_price2.append(results2[i].get("价格"))
    statistics_price = [statistics_price1, statistics_price2]
    return statistics_price

def get_date_PPZSH():
    results = PPZ_data.find({'厂家':'上海石化'}).sort("发布时间", pymongo.DESCENDING).limit(5)
    statistics_date = []
    for i in range(5):
        statistics_date.append(results[i].get("发布时间"))
    return statistics_date