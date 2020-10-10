import pymongo
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import re

plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.project
ICIS = db.ICIS

def get_data_ICIS():
    results = ICIS.find()
    count = ICIS.find().count()
    statistics_price_max = []
    statistics_price_min = []
    statistics_date = []
    for i in range(count - 1, -1, -1):
        statistics_price_max.append(int(results[i].get("priceMax")))
        statistics_price_min.append(int(results[i].get("priceMin")))
        statistics_date.append(results[i].get("date"))
    plt.figure(figsize=(12, 8))
    plt.plot(statistics_date, statistics_price_max, linewidth=2, alpha=0.5)
    plt.plot(statistics_date, statistics_price_min, linewidth=2, alpha=0.5)
    plt.fill_between(statistics_date, statistics_price_max, statistics_price_min, facecolor='blue', alpha=0.1)
    plt.title("BOPP Film：CTR China Import价格变化表——ICIS", fontsize=14)
    plt.xlabel("收盘时间(yyyy-mm-dd)", fontsize=14)
    plt.ylabel("价格（美元/吨）", fontsize=14)
    plt.tick_params(axis='both')
    # ax = plt.gca()
    # ax.xaxis.set_major_locator(MultipleLocator(20))
    # ax.yaxis.set_major_locator(MultipleLocator(100))
    filename = "BOPP Film：CTR China Import价格变化表——ICIS.png"
    plt.savefig(filename)
    plt.show()
    return filename

# 查询ICIS厚光膜近期三天价格
def get_table_ICIS():
    results = ICIS.find().limit(5)
    statistics_price1 = []
    statistics_price2 = []
    for i in range(5):
        statistics_price1.append(str(results[i].get("priceMax")))
        statistics_price2.append(str(results[i].get("priceMin")))
    statistics_price = [statistics_price1, statistics_price2 ]
    return statistics_price

# 查询ICIS厚光膜近期三天时间
def get_date_ICIS():
    results = ICIS.find().limit(5)
    statistics_date = []
    for i in range(5):
        statistics_date.append(results[i].get("date"))
    return statistics_date
