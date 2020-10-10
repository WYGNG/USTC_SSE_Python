# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:52:45 2019

@author: tychou
"""

import pandas as pd
import re

data =pd.read_csv(r'info4.csv',header = 0,encoding="utf-8")
result = pd.DataFrame(data)

#a = result.dropna(axis=0,how='any')
#单位共有三种，万/月、千/月、万/年,以万/月为标准
b0 = u'万/月'
b1 = u'千/月'
b2 = u'万/年'
b3 = u'元/天'
li_salary = result['salary']
for i in range(0,len(li_salary)):
    try:
        if b0 in li_salary[i]:
            x=re.findall(r'\d*\.?\d+',li_salary[i])
            li_salary[i] = str(format(float(x[0]),'.2f')+'-'+format(float(x[1]),'.2f'))
        if b1 in li_salary[i]:
            x=re.findall(r'\d*\.?\d+',li_salary[i])
            #print('1.'+x[0]+'-'+x[1])
            min_ = format(float(x[0])/10,'.2f')
            max_ = format(float(x[1])/10,'.2f')
            li_salary[i] = str(min_+'-'+max_)
        if b2 in li_salary[i]:
            x=re.findall(r'\d*\.?\d+',li_salary[i])
            #print('2.'+x[0]+'-'+x[1])
            min_ = format(float(x[0])/12,'.2f')
            max_ = format(float(x[1])/12,'.2f')
            li_salary[i] = str(min_+'-'+max_)
        if b3 in li_salary[i]:
            x = re.findall(r'\d*\.?\d+',li_salary[i])
            min_ = format(float(x[0])*28/10000,'.2f')
            max_ = format(float(x[0])*31/10000,'.2f')
            li_salary[i] = str(min_+'-'+max_)
    except:
        pass

b1 = u'省'
b2 = u'雄安新区'
li_city = result['city']
for i in range(0,len(li_city)):
    try:
        x=re.findall(r'^\w+',li_city[i])
        li_city[i] = str(x[0])
        if b1 in li_city[i] or b2 in li_city[i]:
            result = result.drop(i,axis=0)
    except:
        pass
for i in range(0,len(li_city)):
    print(li_city[i])
     
b = u'人'
li_education = result['education']
for i in range(0,len(li_education)):
    try:
        if b in li_education[i]:
            result = result.drop(i,axis = 0)
    except:
        pass




result.to_csv('info5.csv',header = 1 ,encoding="utf-8",index=0\
              ,columns=['position','salary','company_name','city','experience','education',\
                        'welfare','company_type','company_scale','company_major'])
