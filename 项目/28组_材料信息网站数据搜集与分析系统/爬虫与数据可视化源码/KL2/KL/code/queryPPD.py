import pymongo
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import re

plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.project
PPD_data = db.PPD

def get_PPD_data():
    results= PPD_data.find({'生产厂家':'绍兴三圆'}).sort("发布时间", pymongo.DESCENDING)
    count = results.count()
    price = []
    date = []
    for i in range(count - 1, -1, -1):
        price.append(int(results[i]['价格']))
        date.append(results[i]['发布时间'])
    plt.figure(figsize=(13, 8))
    plt.plot(date, price, linewidth=2, label="绍兴三圆拉丝")
    plt.legend()
    plt.title("地方(合资）企业PP出厂价格折线图", fontsize=14)
    plt.xlabel("发布时间（年/月/日）", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.yaxis.set_major_locator(MultipleLocator(100))
    plt.tick_params(axis='both')
    filename = "地方（合资）企业PP出厂价格折线图.png"
    plt.savefig(filename)
    plt.show()
    return filename

def get_PPD_data_week():
    results = PPD_data.find({'生产厂家': '绍兴三圆'}).sort("发布时间", pymongo.DESCENDING).limit(7)
    price = []
    date = []
    for i in range(6, -1, -1):
        price.append(int(results[i]['价格']))
        date.append(results[i]['发布时间'])
    plt.figure(figsize=(10, 8))
    plt.plot(date, price, linewidth=2, label="绍兴三圆拉丝")
    plt.legend()
    plt.title("地方（合资）企业PP出厂价格(最近一周）折线图", fontsize=14)
    plt.xlabel("发布时间（年/月/日）", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    plt.tick_params(axis='both')
    filename = "地方（合资）企业PP出厂价格(最近一周）折线图.png"
    plt.savefig(filename)
    plt.show()
    return filename

def get_table_PPD():
    results =PPD_data.find().sort("发布时间", pymongo.DESCENDING).limit(5)
    statistics_price1 = []
    for i in range(5):
        statistics_price1.append(results[i].get("价格"))
    statistics_price = [statistics_price1]
    return statistics_price

def get_date_PPD():
    results =PPD_data.find().sort("发布时间", pymongo.DESCENDING).limit(5)
    statistics_date = []
    for i in range(5):
        statistics_date.append(results[i].get("发布时间"))
    return statistics_date
