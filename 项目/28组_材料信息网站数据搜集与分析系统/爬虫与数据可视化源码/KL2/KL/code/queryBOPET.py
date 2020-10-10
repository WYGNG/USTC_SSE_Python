import pymongo
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import re

plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.project
BOPET_day = db.BOPET_day

# 查询BOPET各个类型膜近一周的价格变化
def get_data_limit_BOPET():
    results = BOPET_day.find().sort("date", pymongo.DESCENDING).limit(7)
    statistics_price1 = []
    statistics_price2 = []
    statistics_price3 = []
    statistics_price4 = []
    statistics_date = []
    for i in range(6, -1, -1):
        data = results[i].get("绍兴翔宇")
        if data:
            statistics_price1.append(int(data.get("12μ印刷膜/镀铝基材")["price"]))
            statistics_price2.append(int(data.get("烫金膜")["price"]))
            statistics_price3.append(int(data.get("厚膜")["price"]))
            statistics_price4.append(int(data.get("转移膜")["price"]))
            statistics_date.append(results[i].get("date"))
    statistics_date=dateSplit(statistics_date)
    plt.figure(figsize=(12, 10))
    plt.subplot(2,2,1)
    plt.plot(statistics_date, statistics_price1, linewidth=2, label="12μ印刷膜/镀铝基材",alpha=0.7)
    plt.title("绍兴翔宇12μ印刷膜/镀铝基材一周收盘价格变化表", fontsize=14)
    plt.xlabel("收盘时间(mm-dd)", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    plt.subplot(2,2,2)
    plt.plot(statistics_date, statistics_price2, linewidth=2, label="烫金膜",alpha=0.7)
    plt.title("绍兴翔宇烫金膜一周收盘价格变化表", fontsize=14)
    plt.xlabel("收盘时间(mm-dd)", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    plt.subplot(2,2,3)
    plt.plot(statistics_date, statistics_price3, linewidth=2, label="厚膜",alpha=0.7)
    plt.title("绍兴翔宇厚膜一周收盘价格变化表", fontsize=14)
    plt.xlabel("收盘时间(mm-dd)", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    plt.subplot(2,2,4)
    plt.plot(statistics_date, statistics_price4, linewidth=2, label="转移膜",alpha=0.7)
    plt.title("绍兴翔宇转移膜一周收盘价格变化表", fontsize=14)
    plt.xlabel("收盘时间(mm-dd)", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    plt.tick_params(axis='both')
    # plt.legend(handles=[line1, line2, line3, line4], labels=["12μ印刷膜/镀铝基材", "烫金膜", "厚膜", "转移膜"])
    filename = "绍兴翔宇BOPET出厂一周收盘价格变化表.png"
    plt.savefig(filename)
    plt.show()
    return filename

def get_data_BOPET(id):
    product_name=''
    if id==1:
        product_name="12μ印刷膜/镀铝基材"
    elif id==2:
        product_name="烫金膜"
    elif id==3:
        product_name="厚膜"
    elif id==4:
        product_name="转移膜"

    results=BOPET_day.find({"date":{'$not':{'$regex':'^2017'}}},{"date","绍兴翔宇."+product_name}).sort("date", pymongo.DESCENDING)
    count=BOPET_day.find({"date":{'$not':{'$regex':'^2017'}}},{"date","绍兴翔宇."+product_name}).count()
    statistics_price=[]
    statistics_date=[]
    for i in range(count-1,-1,-1):
        data=results[i].get("绍兴翔宇")
        if data:
            if data.get(product_name)['price']!='':
                try:
                    statistics_price.append(int(data.get(product_name)["price"]))
                except Exception as e:
                    price_str=data.get(product_name)["price"].split("-")
                    price_avg=( int(price_str[0])+int(price_str[1]))/2
                    statistics_price.append(price_avg)
                statistics_date.append(results[i].get("date"))
    title="绍兴翔宇"+product_name+"历史价格变化表";
    price_max = max(statistics_price)
    price_min = min(statistics_price)
    price_interval = (price_max - price_min) / 20
    date_interval = len(statistics_date) / 10
    plt.figure(figsize=(14, 8))
    plt.plot(statistics_date, statistics_price, linewidth=1)
    plt.title(title, fontsize=14)
    plt.xlabel("收盘时间(yyyy-mm-dd)", fontsize=14)
    plt.ylabel("价格（元/吨）", fontsize=14)
    plt.tick_params(axis='both')
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(date_interval))
    ax.yaxis.set_major_locator(MultipleLocator(price_interval))
    plt.savefig(''.join(re.findall(u'[\u4e00-\u9fa5]', title)) + '.png')
    plt.show()
    return ''.join(re.findall(u'[\u4e00-\u9fa5]',title)) + '.png'

'''小图中横坐标太挤，筛掉时间中的年，只显示月日'''
def dateSplit(date):
    for i in range(0,len(date)):
        temp=date[i].split("-")
        date[i]=temp[1]+"-"+temp[2]
    return date

# 查询BOPET厚光膜当天走势预测
def get_forecast_BOPP():
    results = BOPET_day.find().sort("date", pymongo.DESCENDING).limit(1)
    return results[0]

# 查询BOPET12印刷膜/镀铝基材近期三天价格
def get_table_BOPET():
    results = BOPET_day.find().sort("date", pymongo.DESCENDING).limit(5)
    statistics_price1 = []
    for i in range(5):
        statistics_price1.append(results[i].get("绍兴翔宇").get("12μ印刷膜/镀铝基材")["price"])
    statistics_price = [statistics_price1]
    return statistics_price

# 查询BOPET12印刷膜/镀铝基材近期三天时间
def get_date_BOPET():
    results = BOPET_day.find().sort("date", pymongo.DESCENDING).limit(5)
    statistics_date = []
    for i in range(5):
        statistics_date.append(results[i].get("date"))
    return statistics_date
