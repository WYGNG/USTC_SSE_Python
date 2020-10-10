cities = [('suzhou', 1886760),
          ('shanghai', 1796236),
          ('hangzhou', 1808926),
          ('jiaxing', 1805953),
          ('wuxi', 1790923),
          ('taizhou', 1793505),
          ('changzhou', 1815456),
          ('nanjing', 1799962),
          ('wuhu', 7069199),
          ('nantong', 1799722)]
COLLECTHOURS = 24
CSV_PATH = r'D:\feiwu\csv'
from generateCsv import generate_csv_by_jsonlist
import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from sklearn.svm import SVR
from pyecharts.charts import Geo
from pyecharts import options as opts

def generate_csv():
    # 调用generate_csv_by_jsonlist 10次，产生10个城市的csv提供后面数据分析
    allfilelists = [[] for i in range(len(cities))]
    for i in range(len(cities)):
        for j in range(0, 24):
            string = '0' + str(j) if j < 10 else str(j)
            allfilelists[i].append(cities[i][0] + string + '.json')

    for k in range(len(cities)):
        generate_csv_by_jsonlist(allfilelists[k])

class dataClimate:
    def __init__(self):
        self.df_suzhou = pd.read_csv(r'D:\feiwu\csv\suzhou.csv')
        self.df_shanghai = pd.read_csv(r'D:\feiwu\csv\shanghai.csv')

        self.df_hangzhou = pd.read_csv(r'D:\feiwu\csv\hangzhou.csv')

        self.df_jiaxing = pd.read_csv(r'D:\feiwu\csv\jiaxing.csv')
        self.df_wuxi = pd.read_csv(r'D:\feiwu\csv\wuxi.csv')
        self.df_changzhou = pd.read_csv(r'D:\feiwu\csv\changzhou.csv')
        self.df_taizhou = pd.read_csv(r'D:\feiwu\csv\taizhou.csv')
        self.df_nanjing = pd.read_csv(r'D:\feiwu\csv\nanjing.csv')
        self.df_wuhu = pd.read_csv(r'D:\feiwu\csv\wuhu.csv')
        self.df_nantong = pd.read_csv(r'D:\feiwu\csv\nantong.csv')

    def generateHtml(self):
        datafile = r'D:\feiwu\generateThermodynamicChart.csv'
        data = pd.read_csv(datafile)
        city = data['city']  # 获取名字为flow列的数据
        city_list = city.values.tolist()  # 将csv文件中flow列中的数据保存到列表中

        temp = data['temp']  # 获取名字为flow列的数据
        temp_list = temp.values.tolist()  # 将csv文件中flow列中的数据保存到列表中

        c = (Geo()
             .add_schema(maptype="china")
             .add("温度", [list(z) for z in zip(city_list, temp_list)])
             .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
             .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=30),
                              title_opts=opts.TitleOpts(title="全国部分城市十一月平均最高气温数据分布"),
                              )
             )
        c.render()

    def changeOfOneCity(self):
        y1 = self.df_suzhou['temp']
        x1 = self.df_suzhou['dt']
        day_suzhou = [parser.parse(x) for x in x1]

        fig, ax = plt.subplots()

        # 调整x轴坐标刻度，使其旋转70度，方便查看
        plt.xticks(rotation=70)

        # 设定时间的格式
        hours = mdates.DateFormatter('%H:%M')

        # 设定X轴显示的格式
        ax.xaxis.set_major_formatter(hours)

        # 画出图像，day_milano是X轴数据，y1是Y轴数据，‘r’代表的是'red' 红色
        ax.plot(day_suzhou, y1, 'r')
        plt.savefig(r'D:\feiwu\changeOfOneCity.png')
        plt.close()

    def changeOfSixCities(self):

        y1 = self.df_suzhou['temp']
        x1 = self.df_suzhou['dt']
        y2 = self.df_shanghai['temp']
        x2 = self.df_shanghai['dt']
        y3 = self.df_changzhou['temp']
        x3 = self.df_changzhou['dt']
        y4 = self.df_jiaxing['temp']
        x4 = self.df_jiaxing['dt']
        x4 = self.df_jiaxing['dt']
        y5 = self.df_nanjing['temp']
        x5 = self.df_nanjing['dt']
        y6 = self.df_wuhu['temp']
        x6 = self.df_wuhu['dt']

        df_suzhou = [parser.parse(x) for x in x1]
        df_shanghai = [parser.parse(x) for x in x2]

        df_changzhou = [parser.parse(x) for x in x3]
        df_jiaxing = [parser.parse(x) for x in x4]

        df_nanjing = [parser.parse(x) for x in x5]
        df_wuhu = [parser.parse(x) for x in x6]


        # 调用 subplot 函数, fig 是图像对象，ax 是坐标轴对象
        fig, ax = plt.subplots()

        # 调整x轴坐标刻度，使其旋转70度，方便查看
        plt.xticks(rotation=70)

        # 设定时间的格式
        hours = mdates.DateFormatter('%H:%M')

        # 设定X轴显示的格式
        ax.xaxis.set_major_formatter(hours)

        # 画出图像，day_milano是X轴数据，y1是Y轴数据，‘r’代表的是'red' 红色
        ax.plot(df_suzhou, y1, 'r', df_shanghai, y2, 'r',
                df_changzhou, y3, 'y', df_jiaxing, y4, 'y',
                df_nanjing, y5, 'b', df_wuhu, y6, 'b')
        plt.savefig(r'D:\feiwu\changeOfSixCities.png')
        plt.close()

    def tempMaxAndMinWithDist(self):
        self.dist = [self.df_shanghai['dist'][0],
                     self.df_nantong['dist'][0],
                     self.df_jiaxing['dist'][0],
                     self.df_suzhou['dist'][0],
                     self.df_wuxi['dist'][0],
                     self.df_hangzhou['dist'][0],
                     self.df_changzhou['dist'][0],
                     self.df_taizhou['dist'][0],
                     self.df_nanjing['dist'][0],
                     self.df_wuhu['dist'][0]
                    ]
        self.temp_max = [self.df_shanghai['temp'].max(),
                    self.df_nantong['temp'].max(),
                    self.df_jiaxing['temp'].max(),
                    self.df_suzhou['temp'].max(),
                    self.df_wuxi['temp'].max(),
                    self.df_hangzhou['temp'].max(),
                    self.df_changzhou['temp'].max(),
                    self.df_taizhou['temp'].max(),
                    self.df_nanjing['temp'].max(),
                    self.df_wuhu['temp'].max()
                    ]
        self.temp_min = [self.df_shanghai['temp'].min(),
                    self.df_nantong['temp'].min(),
                    self.df_jiaxing['temp'].min(),
                    self.df_suzhou['temp'].min(),
                    self.df_wuxi['temp'].min(),
                    self.df_hangzhou['temp'].min(),
                    self.df_changzhou['temp'].min(),
                    self.df_taizhou['temp'].min(),
                    self.df_nanjing['temp'].min(),
                    self.df_wuhu['temp'].min()
                    ]

        fig, ax = plt.subplots()
        plt.axis((-10, 350, 18, 23))
        ax.plot(self.dist, self.temp_max, 'ro')
        plt.savefig(r'D:\feiwu\tempMaxWithDist.png')
        plt.close()

        fig, ax = plt.subplots()
        plt.axis((-10, 350, 8, 16))
        ax.plot(self.dist, self.temp_min, 'ro')
        plt.savefig(r'D:\feiwu\tempMinWithDist.png')

        plt.close()

    def LinearRegression(self):
        dist = self.dist[0:10]
        dist = [[x] for x in dist] 
        temp_min = self.temp_min[0:10]
        fig, ax = plt.subplots()
        # 调用SVR函数，在参数中规定了使用线性的拟合函数
        svr_line = SVR(kernel='linear', C=1)
        # 加入数据，进行拟合
        svr_line.fit(dist, temp_min)
        xp = np.arange(10, 350, 10).reshape((-1, 1))
        yp = svr_line.predict(xp)
        # 限制了 x 轴的取值范围
        ax.set_xlim(-10, 350)
        # 画出图像
        ax.plot(self.dist, temp_min, 'ro')
        ax.plot(xp, yp, c='b', label='distance effect')
        plt.savefig(r'D:\feiwu\LinearRegression.png')

        plt.close()

    def humidityOfSixCities(self):
        y1 = self.df_suzhou['humidity']
        x1 = self.df_suzhou['dt']
        y2 = self.df_shanghai['humidity']
        x2 = self.df_shanghai['dt']
        y3 = self.df_hangzhou['humidity']
        x3 = self.df_hangzhou['dt']
        y4 = self.df_jiaxing['humidity']
        x4 = self.df_jiaxing['dt']
        y5 = self.df_taizhou['humidity']
        x5 = self.df_taizhou['dt']
        y6 = self.df_wuhu['humidity']
        x6 = self.df_wuhu['dt']

        fig, ax = plt.subplots()
        plt.xticks(rotation=70)

        df_suzhou = [parser.parse(x) for x in x1]
        df_shanghai = [parser.parse(x) for x in x2]

        df_hangzhou = [parser.parse(x) for x in x3]
        df_jiaxing = [parser.parse(x) for x in x4]

        df_taizhou = [parser.parse(x) for x in x5]
        df_wuhu = [parser.parse(x) for x in x6]

        hours = mdates.DateFormatter('%H:%M')
        ax.xaxis.set_major_formatter(hours)

        ax.plot(df_suzhou, y1, 'r', df_shanghai, y2, 'r',
                df_hangzhou, y3, 'y', df_jiaxing, y4, 'y',
                df_taizhou, y5, 'b', df_wuhu, y6, 'b')
        plt.savefig(r'D:\feiwu\humidityOfSixCities.png')
        plt.close()

    def humidityMaxWithDist(self):
        self.humidity_max = [self.df_shanghai['humidity'].max(),
                         self.df_nantong['humidity'].max(),
                         self.df_jiaxing['humidity'].max(),
                         self.df_suzhou['humidity'].max(),
                         self.df_wuxi['humidity'].max(),
                         self.df_hangzhou['humidity'].max(),
                         self.df_changzhou['humidity'].max(),
                         self.df_taizhou['humidity'].max(),
                         self.df_nanjing['humidity'].max(),
                         self.df_wuhu['humidity'].max()
                         ]
        fig, ax = plt.subplots()
        plt.plot(self.dist, self.humidity_max, 'bo')
        plt.savefig(r'D:\feiwu\humidityMaxWithDist.png')
        plt.close()

    def humidityMinWithDist(self):
        self.humidity_min = [self.df_shanghai['humidity'].min(),
                         self.df_nantong['humidity'].min(),
                         self.df_jiaxing['humidity'].min(),
                         self.df_suzhou['humidity'].min(),
                         self.df_wuxi['humidity'].min(),
                         self.df_hangzhou['humidity'].min(),
                         self.df_changzhou['humidity'].min(),
                         self.df_taizhou['humidity'].min(),
                         self.df_nanjing['humidity'].min(),
                         self.df_wuhu['humidity'].min()
                         ]
        fig, ax = plt.subplots()
        plt.plot(self.dist, self.humidity_min, 'bo')
        plt.savefig(r'D:\feiwu\humidityMinWithDist.png')
        plt.close()

    def roseWind(self):
        hist, bins = np.histogram(self.df_suzhou['deg'], 8, [0, 360])
        self.showRoseWind(hist, 'suzhou', max(hist))

    def showRoseWind(self, values, city_name, max_value):
        N = 8
        theta = np.arange(2 * np.pi / 16, 2 * np.pi, 2 * np.pi / 8)
        radii = np.array(values)

        plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)

        colors = [(1 - x / max_value, 1 - x / max_value, 0.75) for x in radii]

        plt.bar(theta, radii, width=(2 * np.pi / N), bottom=0.0, color=colors)

        plt.savefig(r'D:\feiwu\roseWind.png')
        plt.close()


def main():
    generate_csv()
    c = dataClimate()
    c.generateHtml()
    c.changeOfOneCity()
    c.changeOfSixCities()
    c.tempMaxAndMinWithDist()
    c.LinearRegression()
    c.humidityOfSixCities()
    c.humidityMaxWithDist()
    c.humidityMinWithDist()
    c.roseWind()

if __name__ == '__main__':
    main()