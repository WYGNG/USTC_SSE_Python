import pymongo
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import re

plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.project
BOPP_data = db.BOPP_day

# 查询BOPP厚光膜在各地区近一周的价格变化
def get_data_limit_BOPP():

    statistics_price1 = []
    statistics_price2 = []
    statistics_price3 = []
    statistics_price4 = []
    statistics_price5 = []
    statistics_date = []
    results = BOPP_data.find().sort("datetime", pymongo.DESCENDING).limit(7)
    for i in range(6, -1, -1):
        data = results[i].get("BOPP厚光膜")
        if data:
            statistics_price1.append(int(data.get("华北地区")["价格"]))
            statistics_price2.append(int(data.get("华东地区")["价格"]))
            statistics_price3.append(int(data.get("华南地区")["价格"]))
            statistics_price4.append(int(data.get("东北地区")["价格"]))
            statistics_price5.append(int(data.get("西南地区")["价格"]))
            statistics_date.append(results[i].get("datetime"))
    plt.figure(figsize=(10, 8))
    line1, = plt.plot(statistics_date, statistics_price1, linewidth=2, label="华北地区")
    line2, = plt.plot(statistics_date, statistics_price2, linewidth=2, label="华东地区")
    line3, = plt.plot(statistics_date, statistics_price3, linewidth=2, label="华南地区")
    line4, = plt.plot(statistics_date, statistics_price4, linewidth=2, label="东北地区")
    line5, = plt.plot(statistics_date, statistics_price5, linewidth=2, label="西南地区")
    plt.title("国内BOPP复合膜出厂一周收盘价格变化表", fontsize=14)
    plt.xlabel("收盘时间(yyyy-mm-dd)", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    plt.tick_params(axis='both')
    plt.legend(handles=[line1, line2, line3, line4, line5], labels=["华北地区", "华东地区", "华南地区", "东北地区", "西南地区"])
    filename = "国内BOPP复合膜出厂一周收盘价格变化表.png"
    plt.savefig(filename)
    plt.show()
    return filename

# 查询BOPP厚光膜在华北/华东/华南/东北/西南地区的价格变化
def get_data_BOPP(area):
    results = BOPP_data.find({}, {"BOPP厚光膜." + area, "datetime"}).sort("datetime", pymongo.DESCENDING)
    count = BOPP_data.find({}, {"BOPP厚光膜." + area, "datetime"}).count()
    statistics_price = []
    statistics_date = []
    for i in range(count - 1, -1, -1):
        data = results[i].get("BOPP厚光膜")
        if data:
            statistics_price.append(int(data.get(area)["价格"]))
            statistics_date.append(results[i].get("datetime"))
    plt.figure(figsize=(13, 8))
    plt.plot(statistics_date, statistics_price, linewidth=2)
    plt.title("国内BOPP复合膜出厂收盘价格变化表——" + area, fontsize=14)
    plt.xlabel("收盘时间(yyyy-mm-dd)", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    plt.tick_params(axis='both')
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_major_locator(MultipleLocator(100))
    filename = "国内BOPP复合膜出厂收盘价格变化表——" + area + ".png"
    plt.savefig(filename)
    plt.show()
    return filename


# 查询BOPP厚光膜当天走势预测
def get_forecast_BOPP():
    results = BOPP_data.find().sort("datetime", pymongo.DESCENDING).limit(1)
    return results[0]

# 查询BOPP厚光膜近期三天价格
def get_table_BOPP():
    results = BOPP_data.find().sort("datetime", pymongo.DESCENDING).limit(5)
    statistics_price1 = []
    statistics_price2 = []
    statistics_price3 = []
    statistics_price4 = []
    statistics_price5 = []
    for i in range(5):
        statistics_price1.append(results[i].get("BOPP厚光膜").get("华北地区")["价格"])
        statistics_price2.append(results[i].get("BOPP厚光膜").get("华东地区")["价格"])
        statistics_price3.append(results[i].get("BOPP厚光膜").get("华南地区")["价格"])
        statistics_price4.append(results[i].get("BOPP厚光膜").get("东北地区")["价格"])
        statistics_price5.append(results[i].get("BOPP厚光膜").get("西南地区")["价格"])

    statistics_price = [statistics_price1, statistics_price2, statistics_price3, statistics_price4, statistics_price5]
    return statistics_price


# 查询BOPP厚光膜近期三天时间
def get_date_BOPP():
    results = BOPP_data.find().sort("datetime", pymongo.DESCENDING).limit(5)
    statistics_date = []
    for i in range(5):
        statistics_date.append(results[i].get("datetime"))
    return statistics_date
