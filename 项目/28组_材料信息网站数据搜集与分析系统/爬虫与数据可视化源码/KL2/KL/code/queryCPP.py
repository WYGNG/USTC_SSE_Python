import pymongo
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import re

plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.project
CPP_data = db.CPP_day

# 查询CPP复合膜/CPP镀铝基材/CPP蒸煮膜在各地区近一周的价格变化
def get_data_limit_CPP(product):
    results = CPP_data.find().sort("datetime", pymongo.DESCENDING).limit(7)
    statistics_price1 = []
    statistics_price2 = []
    statistics_price3 = []
    statistics_date = []
    for i in range(6, -1, -1):
        data = results[i].get(product)
        if data:
            statistics_price1.append(int(data.get("华北地区")["价格"]))
            statistics_price2.append(int(data.get("华东地区")["价格"]))
            if data.get("华南地区"):
                statistics_price3.append(int(data.get("华南地区")["价格"]))
            statistics_date.append(results[i].get("datetime"))
    plt.figure(figsize=(12, 8))
    line1, = plt.plot(statistics_date, statistics_price1, linewidth=2, label="华北地区")
    line2, = plt.plot(statistics_date, statistics_price2, linewidth=2, label="华东地区")
    if not statistics_price3:
        plt.legend(handles=[line1, line2], labels=["华北地区", "华东地区"])
    else:
        line3, = plt.plot(statistics_date, statistics_price3, linewidth=2, label="华南地区")
        plt.legend(handles=[line1, line2, line3, ], labels=["华北地区", "华东地区", "华南地区"])

    plt.title("国内" + product + "出厂一周收盘价格变化表", fontsize=14)
    plt.xlabel("收盘时间(yyyy-mm-dd)", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    plt.tick_params(axis='both')
    filename = "国内" + product + "出厂一周收盘价格变化表.png"
    plt.savefig(filename)
    plt.show()
    return filename

# 查询CPP复合膜/CPP镀铝基材/CPP蒸煮膜在华北/华东/华南/东北/西南地区的价格变化
def get_data_CPP(product):
    results = CPP_data.find({}, {product, "datetime"}).sort("datetime", pymongo.DESCENDING)
    count = CPP_data.find({}, {product, "datetime"}).count()
    statistics_price1 = []
    statistics_price2 = []
    statistics_price3 = []
    statistics_date = []
    for i in range(count - 1, -1, -1):
        data = results[i].get(product)
        if data:
            statistics_price1.append(int(data.get("华北地区")["价格"]))
            statistics_price2.append(int(data.get("华东地区")["价格"]))
            if data.get("华南地区"):
                statistics_price3.append(int(data.get("华南地区")["价格"]))
            statistics_date.append(results[i].get("datetime"))
    plt.figure(figsize=(11, 8))
    line1, = plt.plot(statistics_date, statistics_price1, linewidth=2, label="华北地区")
    line2, = plt.plot(statistics_date, statistics_price2, linewidth=2, label="华东地区")
    if not statistics_price3:
        plt.legend(handles=[line1, line2], labels=["华北地区", "华东地区"])
    else:
        line3, = plt.plot(statistics_date, statistics_price3, linewidth=2, label="华南地区")
        plt.legend(handles=[line1, line2, line3, ], labels=["华北地区", "华东地区", "华南地区"])

    plt.title("国内" + product + "出厂收盘价格变化表", fontsize=14)
    plt.xlabel("收盘时间(yyyy-mm-dd)", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    plt.tick_params(axis='both')
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(25))
    ax.yaxis.set_major_locator(MultipleLocator(100))
    filename = "国内" + product + "出厂收盘价格变化表.png"
    plt.savefig(filename)
    plt.show()
    return filename

# 查询CPP厚光膜当天走势预测
def get_forecast_CPP():
    results = CPP_data.find().sort("datetime", pymongo.DESCENDING).limit(1)
    return results[0]

# 查询CPP厚光膜近期三天价格
def get_table_CPP():
    results = CPP_data.find().sort("datetime", pymongo.DESCENDING).limit(5)
    statistics_price1 = []
    statistics_price2 = []
    statistics_price3 = []
    statistics_price4 = []
    statistics_price5 = []
    statistics_price6 = []
    statistics_price7 = []
    statistics_price8 = []
    for i in range(5):
        statistics_price1.append(results[i].get("CPP复合膜").get("华北地区")["价格"])
        statistics_price2.append(results[i].get("CPP复合膜").get("华东地区")["价格"])
        statistics_price3.append(results[i].get("CPP复合膜").get("华南地区")["价格"])
        statistics_price4.append(results[i].get("CPP镀铝基材").get("华北地区")["价格"])
        statistics_price5.append(results[i].get("CPP镀铝基材").get("华东地区")["价格"])
        statistics_price6.append(results[i].get("CPP镀铝基材").get("华南地区")["价格"])
        statistics_price7.append(results[i].get("CPP蒸煮膜").get("华北地区")["价格"])
        statistics_price8.append(results[i].get("CPP蒸煮膜").get("华东地区")["价格"])

    statistics_price = [statistics_price1, statistics_price2, statistics_price3, statistics_price4, statistics_price5, statistics_price6, statistics_price7, statistics_price8]
    return statistics_price


# 查询CPP厚光膜近期三天时间
def get_date_CPP():
    results = CPP_data.find().sort("datetime", pymongo.DESCENDING).limit(5)
    statistics_date = []
    statistics_date.append("地区")
    for i in range(5):
        statistics_date.append(results[i].get("datetime"))
    return statistics_date
