import csv
import matplotlib.pyplot as plt
import os
import jieba
import jieba.analyse
from wordcloud import WordCloud, STOPWORDS
import numpy    #numpy计算包
from datetime import datetime
import re

#时间与电影数量折线图
def movie_date_amount(fileName):
    #获取每列
    with open(fileName, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        header_row[0] = header_row[0][2:-1]
        #print(header_row)
        '''
        for index, column_header in enumerate(header_row):
             print(index, column_header)
        '''
        #对数据进行筛选生成对应坐标数组
        dict1 = {}
        keys,data = [],[]
        for row in reader:
            if row[18] in dict1.keys():
                dict1[row[18]] = dict1[row[18]]+1
            else:
                dict1.setdefault(row[18],1)
        dict1.pop('0')
        for key in dict1.keys():
            keys.append(key)
            data.append(dict1[key])
    #创建画板
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fig1 = plt.figure(figsize=(30,5))
    plt.xticks(size='small', rotation=90, fontsize=5)
    #plt.plot(横坐标数组，纵坐标数组，颜色)
    plt.plot(keys,data,'red')
    plt.title("年份与电影数量图")
    #plt.show()
    pic_path = "D:/Python_Programs/Lab/result/movie_date_amount.png"
    plt.savefig(pic_path)

#个别国家的时间与电影数量折线图
def area_date_amount(filename):
    with open(fileName, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        header_row[0] = header_row[0][2:-1]
        list_Chian = []
        list_USA = []
        list_India = []
        for row in reader:
            if '中国大陆' in row[13]:
                list_Chian.append(row)
            elif '美国' in row[13]:
                list_USA.append(row)
            elif '印度' in row[13]:
                list_India.append(row)
        dict1,dict2,dict3 = {},{},{}
        for list in list_Chian:
            if list[18] in dict1.keys():
                dict1[list[18]] = dict1[list[18]]+1
            else:
                dict1.setdefault(list[18],1)
        for list in list_USA:
            if list[18] in dict2.keys():
                dict2[list[18]] = dict2[list[18]]+1
            else:
                dict2.setdefault(list[18],1)
        for list in list_India:
            if list[18] in dict3.keys():
                dict3[list[18]] = dict3[list[18]]+1
            else:
                dict3.setdefault(list[18],1)
        time,amount1,amount2,amount3 = [],[],[],[]
        for key in dict1.keys():
            time.append(key)
            amount1.append(dict1[key])
        set_index = []
        for index,year in enumerate(time):
            if year in dict2.keys():
                amount2.append(dict2[year])
            else:
                set_index.append(index)
        for it in set_index:
            time.pop(it)
            amount1.pop(it)
            for i in range(len(set_index)):
                set_index[i] -= 1
        set_index2 = []
        for index, year in enumerate(time):
            if year in dict3.keys():
                amount3.append(dict3[year])
            else:
                set_index2.append(index)
        for it in set_index2:
            time.pop(it)
            amount2.pop(it)
            amount1.pop(it)
            for i in range(len(set_index2)):
                set_index2[i] -= 1
        time.pop()
        amount1.pop()
        amount2.pop()
        amount3.pop()
        # 创建画板
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        fig1 = plt.figure(figsize=(15, 5))
        plt.xticks(size='small', rotation=90, fontsize=10)
        # plt.plot(横坐标数组，纵坐标数组，颜色)
        plt.plot(time, amount1, '-',label='中国')
        plt.plot(time, amount2, '-',label='美国')
        plt.plot(time, amount3, '-',label='印度')
        plt.xticks(time)
        plt.xlabel('年份')
        plt.title("各地区年份与电影数量图")
        #显示每条线的label
        plt.legend()
        #plt.show()
        pic_path = "D:/Python_Programs/Lab/result/area_date_amount.png"
        plt.savefig(pic_path)

#语言与电影数量柱状图
def lan_amount(filename):
    with open(fileName, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        header_row[0] = header_row[0][2:-1]
        dict1 = {}
        list_lans_amount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        list_lans = ['汉语','英语','法语','德语','韩语','意大利语','日语','葡萄牙语','泰语','罗马尼亚语','阿拉伯语','尼泊尔语','丹麦语','捷克语']
        for row in reader:
            if '汉语' in row[10] or '粤语' in row[10] or '闽南' in row[10] or '藏语' in row[10]:
                list_lans_amount[0] += 1
            elif '英语' in row[10]:
                list_lans_amount[1] += 1
            elif '法语' in row[10]:
                list_lans_amount[2] += 1
            elif '德语' in row[10]:
                list_lans_amount[3] += 1
            elif '韩语' in row[10]:
                list_lans_amount[4] += 1
            elif '意大利语' in row[10]:
                list_lans_amount[5] += 1
            elif '日语' in row[10]:
                list_lans_amount[6] += 1
            elif '葡萄牙语' in row[10]:
                list_lans_amount[7] += 1
            elif '泰语' in row[10]:
                list_lans_amount[8] += 1
            elif '罗马尼亚语' in row[10]:
                list_lans_amount[9] += 1
            elif '阿拉伯语' in row[10]:
                list_lans_amount[10] += 1
            elif '尼泊尔语' in row[10]:
                list_lans_amount[11] += 1
            elif '丹麦语' in row[10]:
                list_lans_amount[12] += 1
            elif '捷克语' in row[10]:
                list_lans_amount[13] += 1
        # 创建画板
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        fig1 = plt.figure(figsize=(15, 6))
        plt.xticks(size='small', rotation=90, fontsize=8)
        # plt.bar(横坐标数组，纵坐标数组)
        plt.bar(list_lans, list_lans_amount,alpha=0.5, width=0.3, color='yellow', edgecolor='red', label='语言与电影数量图', lw=1)
        plt.title("语言与电影数量图")
        plt.legend()
        #plt.show()
        pic_path = "D:/Python_Programs/Lab/result/lan_amount.png"
        plt.savefig(pic_path)

#语言与电影数量饼状图
def lan_amount_pie(filename):
    with open(fileName, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        header_row[0] = header_row[0][2:-1]
        dict1 = {}
        list_lans_amount = [0,0,0,0,0,0,0,0,0,0]
        list_lans = ['汉语','英语','法语','德语','韩语','意大利语','西班牙语','日语','瑞典语','其他']
        for row in reader:
            if ('汉语' in row[10]) or ('普通话' in row[10]) or ('粤语' in row[10]) or ('闽南' in row[10])or('上海' in row[10]) or ('藏语' in row[10]) or ('方言' in row[10]) or ('彝语' in row[10]) or ('客家话' in row[10]) or ('武汉话' in row[10]):
                list_lans_amount[0] += 1
            elif '英语' in row[10]:
                list_lans_amount[1] += 1
            elif '法语' in row[10]:
                list_lans_amount[2] += 1
            elif '德语' in row[10]:
                list_lans_amount[3] += 1
            elif '韩语' in row[10]:
                list_lans_amount[4] += 1
            elif '意大利语' in row[10]:
                list_lans_amount[5] += 1
            elif '葡萄牙语' in row[10]:
                list_lans_amount[6] += 1
            elif '日语' in row[10]:
                list_lans_amount[7] += 1
            elif '瑞典语' in row[10]:
                list_lans_amount[8] += 1
            elif row[10] != '':
                list_lans_amount[9] += 1
                if row[10] in dict1.keys():
                    dict1[row[10]] = dict1[row[10]] + 1
                else:
                    dict1.setdefault(row[10], 1)
        # 创建画板
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        fig1 = plt.figure(figsize=(8, 6))
        #plt.xticks(size='small', rotation=90, fontsize=7)
        explode = (0,0,0,0,0,0,0,0,0,0)
        plt.pie(list_lans_amount,explode=explode,labels=list_lans,autopct='%1.1f%%',shadow=False,startangle=150,
                textprops={'fontsize':10,'color':'black'})
        plt.title("语言与电影数量饼状图")
        #plt.show()
        pic_path = "D:/Python_Programs/Lab/result/lan_amount_pie.png"
        plt.savefig(pic_path)

#国家与电影数量柱状图
def area_amount(filename):
    with open(fileName, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        header_row[0] = header_row[0][2:-1]
        list_area_amount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        list_areas = ['中国','美国','日本','韩国','印度','意大利','加拿大','西班牙','巴西','英国','德国','法国','俄罗斯','瑞典','澳大利亚']
        for row in reader:
            if '中国' in row[13] :
                list_area_amount[0] += 1
            elif '美国' in row[13]:
                list_area_amount[1] += 1
            elif '日本' in row[13]:
                list_area_amount[2] += 1
            elif '韩国' in row[13]:
                list_area_amount[3] += 1
            elif '印度' in row[13]:
                list_area_amount[4] += 1
            elif '意大利' in row[13]:
                list_area_amount[5] += 1
            elif '加拿大' in row[13]:
                list_area_amount[6] += 1
            elif '西班牙' in row[13]:
                list_area_amount[7] += 1
            elif '巴西' in row[13]:
                list_area_amount[8] += 1
            elif ('英国' in row[13]) or ('爱尔兰' in row[13]):
                list_area_amount[9] += 1
            elif '德国' in row[13]:
                list_area_amount[10] += 1
            elif '法国' in row[13]:
                list_area_amount[11] += 1
            elif '俄罗斯' in row[13]:
                list_area_amount[12] += 1
            elif '瑞典' in row[13]:
                list_area_amount[13] += 1
            elif '澳大利亚' in row[13]:
                list_area_amount[14] += 1

        # 创建画板
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        fig1 = plt.figure(figsize=(15, 6))
        plt.xticks(size='small', rotation=90, fontsize=8)
        # plt.bar(横坐标数组，纵坐标数组)
        plt.bar(list_areas, list_area_amount,alpha=0.5, width=0.3, color='yellow', edgecolor='red', label='国家与电影数量图', lw=1)
        plt.title("国家与电影数量柱状图")
        plt.legend()
        #plt.show()
        pic_path = "D:/Python_Programs/Lab/result/area_amount.png"
        plt.savefig(pic_path)

#评分和电影数柱状图
def score_count(fileName):
    dict1={}
    score,amount = [],[]
    with open(fileName, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        header_row[0] = header_row[0][2:-1]
        print(header_row)
        for row in reader:
            if row[6] in dict1.keys():
                dict1[row[6]] += 1;
            elif row[6] != '0.0':
                dict1.setdefault(row[6],1)
        for key in dict1.keys():
            score.append(key)
            amount.append(dict1[key])
    # 创建画板
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fig1 = plt.figure(figsize=(15, 6))
    plt.xticks(size='small', rotation=90, fontsize=8)
    # plt.bar(横坐标数组，纵坐标数组)
    plt.bar(score, amount, alpha=0.5, width=0.3, color='yellow', edgecolor='red',
             label='评分与电影数量柱状图', lw=1)
    plt.title("评分与电影数量柱状图")
    plt.legend()
    #plt.show()
    pic_path = "D:/Python_Programs/Lab/result/score_count.png"
    plt.savefig(pic_path)

#不同国家每年发行电影的平均评分
def date_averageScover(filename):
    country = ['中国','美国','日本','韩国']
    date = []
    for i in range(1948,2020):
        date.append(i)
    list_Chian = []
    list_USA = []
    list_Japan = []
    with open(fileName, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        header_row[0] = header_row[0][2:-1]
        for row in reader:
            if '中国' in row[13]:
                list_Chian.append(row)
            elif '美国' in row[13]:
                list_USA.append(row)
            elif '日本' in row[13]:
                list_Japan.append(row);
    Ave_China = []
    Ave_USA = []
    Ave_Japan = []
    for year in date:
        sum,count = 0,0
        average = 0
        for row in list_Chian:
            if (str(year) in row[18]) and (row[6] != '0.0'):
                count += 1
                sum += float(row[6])
        if(count > 0):
            average = sum / count
        Ave_China.append(average)
    for year in date:
        sum,count = 0,0
        average = 0
        for row in list_USA:
            if (str(year) in row[18]) and (row[6] != '0.0'):
                count += 1
                sum += float(row[6])
        if (count > 0):
            average = sum / count
        Ave_USA.append(average)
    for year in date:
        sum,count = 0,0
        average = 0
        for row in list_Japan:
            if (str(year) in row[18]) and (row[6] != '0.0'):
                count += 1
                sum += float(row[6])
        if (count > 0):
            average = sum / count
        Ave_Japan.append(average)
    # 创建画板
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fig1 = plt.figure(figsize=(15, 5))
    plt.xticks(size='small', rotation=90, fontsize=10)
    # plt.plot(横坐标数组，纵坐标数组，颜色)
    plt.plot(date, Ave_China, '-', label='中国')
    plt.plot(date, Ave_USA, '-', label='美国')
    plt.plot(date, Ave_Japan, '-', label='日本')
    plt.xticks(date)
    plt.xlabel('年份')
    plt.title("部分国家年份与平均评分折线图")
    # 显示每条线的label
    plt.legend()
    #plt.show()
    pic_path = "D:/Python_Programs/Lab/result/date_averageScover.png"
    plt.savefig(pic_path)

#生成豆瓣评分top20的电影csv文件
def createtop20(filename):
    data = csv.reader(open(filename,encoding='utf-8'), delimiter=',')
    sortedlist = sorted(data, key=lambda x: x[6], reverse=True)
    #按评分排列所有影片，取评分前20生成score_top20.csv
    with open("score_top20.csv", "w",encoding='utf-8-sig', newline='') as f:
        fileWriter = csv.writer(f, delimiter=',')
        for i in range (1,21):
            #print(row)
            fileWriter.writerow(sortedlist[i])
    f.close()

#评分top20生成词云
def createwordcloud(filename1,filename2):
    data = csv.reader(open(filename1, encoding='utf-8'), delimiter=',')
    movie_id = []
    for row in data:
        #print(row[0])
        movie_id.append(row[0])
    #根据id对每个top20电影生成词云

    #获取评论
    for id in movie_id:
        data = csv.reader(open(filename2, encoding='utf-8'), delimiter=',')
        txtname = "tmp"+id.encode('utf-8').decode('utf-8-sig')+".txt"
        flag = os.path.exists(txtname)
        if flag != True:
            for row in data:
                if row[2] == id:
                    f = open(txtname, "a", encoding='utf-8-sig')
                    f.write(row[3])

    #生成词云
    for id in movie_id:
        txtname = 'tmp'+id.encode('utf-8').decode('utf-8-sig')+'.txt'
        flag = os.path.exists(txtname)
        if flag:
            data = open(txtname.encode('utf-8').decode('utf-8-sig'), encoding='utf-8-sig').read()
            #print(type(data))
            pattern = re.compile(r'[\u4e00-\u9fa5]+')
            filterdata = re.findall(pattern, data)
            cleaned_comments = ''.join(filterdata)
            # 使用jieba分词进行中文分词,topK为返回关键词个数,withWeight为是否一并返回关键词权重值,默认值为 False
            result=jieba.analyse.textrank(cleaned_comments,topK=80,withWeight=True)
            keywords = dict()
            for i in result:
                keywords[i[0]] = i[1]
            print("删除停用词前", keywords)  # {'演员': 0.18290354231824632, '大片': 0.2876433001472282}
            # 停用词集合
            stopwords = set(STOPWORDS)
            f = open('./StopWords.txt', encoding="utf8")
            while True:
                word = f.readline()
                if word == "":
                    break
                stopwords.add(word[:-1])

            keywords = {x: keywords[x] for x in keywords if x not in stopwords}
            print("\n删除停用词后", keywords)
            # 用词云进行显示,font_path字体路径
            wordcloud = WordCloud(font_path="simhei.ttf", background_color="white",
                                  max_font_size=80, stopwords=stopwords)
            word_frequence = keywords
            myword = wordcloud.fit_words(word_frequence)
            plt.imshow(myword)  # 展示词云图
            plt.axis("off")
            #plt.show()
            pic_path = "D:/Python_Programs/Lab/result/wordcloud"+id.encode('utf-8').decode('utf-8-sig')+'.png'
            plt.savefig(pic_path)


fileName = 'moviedata\movies.csv'
fileName1= 'moviedata\comments.csv'
fileName2 = 'score_top20.csv'
'''
movie_date_amount(fileName)
area_date_amount(fileName)
lan_amount(fileName)
lan_amount_pie(fileName)
area_amount(fileName)
score_count(fileName)
date_averageScover(fileName)
createtop20(fileName)
'''
createwordcloud(fileName2,fileName1)



