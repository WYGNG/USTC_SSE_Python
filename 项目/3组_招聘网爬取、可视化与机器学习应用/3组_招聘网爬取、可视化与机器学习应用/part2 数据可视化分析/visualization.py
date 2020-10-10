# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import re
#from pyecharts import Pie
from pyecharts import Pie,Geo,WordCloud,Bar3D,Line
import matplotlib.pyplot as plt

file =pd.read_csv(r'info5.csv',header = 0,encoding="utf-8")
f = pd.DataFrame(file)
pd.set_option('display.max_rows',None)

pos = f['position']
sal = f['salary']
cN= f['company_name']
ct = f['city']
exp= f['experience']
edu = f['education']
wel = f['welfare']
cT=f['company_type']
cS = f['company_scale']
cM = f['company_major']

#1-初始化操作
position =[]
salary = []
companyName = []
city = []
experience =[]
education =[]
welfare = []
companyType = []
companyScale =[]
companyMajor = []
for i in range(0,len(f)):
    try:
        position.append(pos[i])
        companyName.append(cN[i])
        city.append(ct[i])
        experience.append(exp[i])
        education.append(edu[i])
        welfare.append(wel[i])
        companyType.append(cT[i])
        companyScale.append(cS[i])
        companyMajor.append(cM[i])       
        #print(position[i])     
        s = re.findall(r'\d*\.?\d+',sal[i])
        salary.append([float(s[0]),float(s[1])])
    except:
        pass
#1-end
#2-折线图1
#输入str为关系表中任意字段，object为str所对应的list,order需为str字段所有value，使折线图x轴按order顺序
def linearGraph(str,object,order):
    plt.rcParams['font.family'] = 'STSong'
    plt.rcParams['font.size'] =10
    min_s=[]
    max_s=[]
    for i in range(0,len(experience)):
        min_s.append(salary[i][0])
        max_s.append(salary[i][1])
    my_df = pd.DataFrame({str:object,'min_salary':min_s,"max_salary":max_s})
    data = my_df.groupby(str).mean()['min_salary']
    data = data[order]
    data.plot(kind='line')
    plt.savefig('111'+str+"-工资线状图.jpg")
    plt.show()
#2-end
'''
order1 =['无工作经验','1年经验','2年经验','3-4年经验','5-7年经验','8-9年经验','10年以上经验']
linearGraph('experience',experience,order1)
order2=['初中及以下','中专','大专','高中','本科','硕士']
linearGraph('education',education,order2)
'''
#显示列属性值以及出现的数量
def columnsAndCount(list):
    list_temp={}
    for i in set(list):
        list_temp[i]=list.count(i)
    return list_temp
#3-玫瑰环图
def ringFigure(str,object):
    obj=columnsAndCount(object)
    attr = obj.keys()
    value = obj.values()
    pie =Pie(str,width=1000,height=500)
    
    pie.add(str,attr,value,\
            center=[70,50],is_random=False,\
            radius=[30,75],rosetype='radius',\
            is_lengend_show=True,is_label_show=True,is_legend_orient='vertical')
    pie.render('111'+str+'玫瑰环图.html')
#3-end
'''
ringFigure('学历要求',education)
'''

#4-词云
def wordloud(str,x,y):
    wordcloud = WordCloud(background_color="#white",\
                          width = 1300,height = 800)
    wordcloud.add("",x,y,word_size_range=[10,20],rotate_step=150,shape="star")
    wordcloud.render(str+"词云.html")
#4-end
'''
comValue = []
comValue = columnsAndCount(companyName)
x = []
y = []
for i in set(comValue):
    x.append(i)
    y.append(comValue[i])
wordloud('公司',x,y)

comValue = []
comValue = columnsAndCount(position)
x = []
y = []
for i in set(comValue):
    x.append(i)
    y.append(comValue[i])
wordloud('职位',x,y)
'''
#5-折线图2
def Linef(str,x,y):
    line = Line(str)
    line.add(str,x,y,is_symbol_show=True,        
             is_smooth=False,
             is_stack=True,
             is_step=False,
             is_fill=True,)
    line.render(str+'.html')
#5-end
'''
min_s=[]
max_s=[]
for i in range(0,len(experience)):
    min_s.append(salary[i][0])
    max_s.append(salary[i][1])
my_df = pd.DataFrame({'experience':experience,'min_salary':min_s,"max_salary":max_s})
data1 = my_df.groupby('experience').mean()['min_salary']
order1 =['无工作经验','1年经验','2年经验','3-4年经验','5-7年经验','8-9年经验','10年以上经验']
data1 =data1[order1]
Linef("工作经验工作线状图",order1,data1)

my_df2 = pd.DataFrame({'education':education,'min_salary':min_s,"max_salary":max_s})
data2 = my_df2.groupby('education').mean()['min_salary']
order2=['初中及以下','中专','大专','高中','本科','硕士']
data2 =data2[order2]
Linef("学历线状图",order2,data2)
'''

#6-Geo地图
def geoprint(str,attr,value):
    geo = Geo(str,title_color="#fff",\
              title_text_size=24,title_top=20,title_pos="center",\
              width=1300,height=600) 
    geo.add(str,attr,value,\
            type="effectScatter",is_random=True,visual_range=[0,1000],\
            maptype="china",symbol_size=8,effect_scale=5,border_color="#000000",is_visualmap=True)
    geo.render(str+".html")
#6-end
'''
elements_city=[]
elements_city=pd.DataFrame({'city':city}).groupby('city').count().index
address=elements_city
min_s=[]
max_s=[]
for i in range(0,len(city)):
    min_s.append(salary[i][0])
    max_s.append(salary[i][1])
my_df = pd.DataFrame({'city':city,'min_salary':min_s,"max_salary":max_s})
data1 = my_df.groupby('city').mean()['min_salary']
data2 = my_df.groupby('city').mean()['max_salary']
data = []
for i in range(0,len(data1)):
    data.append(format(data2[i],'.2f'))
value = data    
geoprint("java人才分布",address,value)
'''
#7-3D柱状图
def threeD(str,x_order,y_order,z_order):
    bar3d = Bar3D(background_color="#white",width = 1300,height = 800)
    bar3d.add("城市职位薪水3D柱状图",x_order,y_order,z_order,grid3d_opacity=0.8,grid3d_shading="realistic")
    bar3d.render("城市职位薪水3D柱状图.html")
'''
#数据处理
min_s = []
max_s = []
for i in range(0,len(f)):
    min_s.append(salary[i][0])
    max_s.append(salary[i][1])
poistion_salaryMin = pd.DataFrame({'city':city,'position':position,'min_salary':min_s})
data1 = poistion_salaryMin.groupby('position').mean()['min_salary']
poistion_salaryMax = pd.DataFrame({'position':position,'max_salary':max_s})
data2 = poistion_salaryMax.groupby('position').mean()['max_salary']

elements_poistion = []
elements_poistion = data1.keys()

elements_city=[]
elements_city=pd.DataFrame({'city':city}).groupby('city').count().index

elements_education=[]
elements_education=pd.DataFrame({'education':education}).groupby('education').count().index

city_position_salarySum=[]
for i in range(0,len(elements_city)):
    for j in range(0,len(elements_poistion)):
        city_position_salarySum.append([0,0.00,0.00,elements_city[i],elements_poistion [j]])

for i in range(0,len(f)):
    for j in range(0,len(city_position_salarySum)):
        if city[i] in city_position_salarySum[j] and position[i] in city_position_salarySum[j]:
            city_position_salarySum[j][0] = city_position_salarySum[j][0]+1
            city_position_salarySum[j][1] = city_position_salarySum[j][1]+min_s[i]            
            city_position_salarySum[j][2] = city_position_salarySum[j][2]+max_s[i]
            break

for i in range(0,len(city_position_salarySum)):
    if city_position_salarySum[i][0] != 0:
        city_position_salarySum[i][1] = format(city_position_salarySum[i][1] / city_position_salarySum[i][0],'.2f')
        city_position_salarySum[i][2] = format(city_position_salarySum[i][2] / city_position_salarySum[i][0],'.2f')

education_position_salarySum=[]
for i in range(0,len(elements_education)):
    for j in range(0,len(elements_poistion)):
        education_position_salarySum.append([0,0.00,0.00,elements_education[i],elements_poistion[j]])

for i in range(0,len(f)):
    for j in range(0,len(education_position_salarySum)):
        if education[i] in education_position_salarySum[j] and position[i] in education_position_salarySum[j]:
            education_position_salarySum[j][0] = education_position_salarySum[j][0]+1
            education_position_salarySum[j][1] = education_position_salarySum[j][1]+min_s[i]            
            education_position_salarySum[j][2] = education_position_salarySum[j][2]+max_s[i]
            break

for i in range(0,len(education_position_salarySum)):
    if education_position_salarySum[i][0] != 0:
        education_position_salarySum[i][1] = format(education_position_salarySum[i][1] / education_position_salarySum[i][0],'.2f')
        education_position_salarySum[i][2] = format(education_position_salarySum[i][2] / education_position_salarySum[i][0],'.2f')

z_order=[]
tem =[]
for i in range(0,len(elements_city)):  
    for j in range(0,len(elements_poistion)):   
        for m in range(0,len(city_position_salarySum)):
            if elements_city[i] in city_position_salarySum[m] and elements_poistion[j] in city_position_salarySum[m]:
                z_order.append([elements_city[i],elements_poistion[j],city_position_salarySum[m][1]])
                break
threeD(str,elements_city,elements_poistion,z_order)
'''
#7-end
