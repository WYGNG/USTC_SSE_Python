import pandas as pd
import json
import numpy

fileslist = ['data.json', 'data_cur.json']

keys_values_array = []
#获取键
temp = json.load(open(fileslist[0], 'r'))

json_fkey_dict = temp['main']
json_keys_main = [str(json_) for json_ in json_fkey_dict.keys()]
json_values_main = [int(j_value) for j_value in json_fkey_dict.values()]

json_fkey_dict = temp['wind']
json_keys_wind = [str(json_) for json_ in json_fkey_dict.keys()]
json_values_wind = [int(j_value) for j_value in json_fkey_dict.values()]



json_keys = json_keys_main.extend(json_keys_wind)
json_keys = json_keys_main
json_values = json_values_main.extend(json_values_wind)
json_values = json_values_main

json_keys.append('name')
json_values.append(temp['name'])

print(json_keys)
print(json_values)

keys_values_array = []
keys = pd.Series(json_keys,name='key')    #这里使用pandas的Series方法对数据进行封装，并命名列名
values = pd.Series(json_values,name='values')
keys_values_array.append(keys)
keys_values_array.append(values)
df_data = numpy.array(keys_values_array)
df = pd.DataFrame(df_data)
#df_data = pd.concat([keys,values],axis=0)  #concat是将多条series数据合并成dataframe，axis参数决定合并的轴向，1代表从第二维度合并，0代表第一维度。
df.to_csv('data4.csv',index=True) #index参数代表不将序列号填入文件，dataframe默认是会生成序列号的

