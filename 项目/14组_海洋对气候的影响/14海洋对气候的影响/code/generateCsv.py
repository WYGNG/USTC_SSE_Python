#把每个城市的10个json文件汇总成csv文件
import pandas as pd
import json
import os
import math
import time
DATA_PATH = r'D:\feiwu\data'
CSV_PATH = r'D:\feiwu\csv'

def generate_csv_by_jsonlist(jsonlist):
    fileslist= jsonlist
    frames = []

    #遍历所有文件，读取数据并写入csv文件
    for i in range(len(fileslist)):
        temp = json.load(open(os.path.join(DATA_PATH, fileslist[i]), 'r'))
        json_fkey_dict = temp['main']
        json_keys_main = [str(json_) for json_ in json_fkey_dict.keys()][0:5]
        json_values_main = [(j_value) for j_value in json_fkey_dict.values()][0:5]
        json_values_main[0] = json_values_main[0] - 273.15

        json_fkey_dict = temp['wind']
        json_keys_wind = [str(json_) for json_ in json_fkey_dict.keys()]
        json_values_wind = [(j_value) for j_value in json_fkey_dict.values()]

        json_keys = json_keys_main.extend(json_keys_wind)
        json_keys = json_keys_main
        json_values = json_values_main.extend(json_values_wind)
        json_values = json_values_main

        json_keys.append('name')
        json_values.append(temp['name'])

        #把时间写入文件
        json_keys.append('dt')
        dt = temp['dt']
        time_local = time.localtime(int(dt))
        cur_index_hour_min = time.strftime("%Y/%m/%d %H:%M:%S",time_local)
        json_values.append(cur_index_hour_min)

        #把和上海的距离写入文件
        lon = -temp['coord']['lon']
        lat = temp['coord']['lat']
        d = distToShanghai(math.radians(lat), math.radians(lon))
        json_keys.append('dist')
        json_values.append(d)

        dict1 = dict(zip(json_keys, json_values))

        df = pd.DataFrame(dict1, index=[i])
        frames.append(df)

    result = pd.concat(frames, sort=True)
    result.to_csv(os.path.join(CSV_PATH, jsonlist[0][:-7] + '.csv'), index=True)

def distToShanghai(lat, lon):

    latShanghai = math.radians(31.22)
    lonShanghai = math.radians(-121.46)
    r = 6371.0
    d = r * math.acos(math.sin(lonShanghai) * math.sin(lon) +
                      math.cos(lonShanghai) * math.cos(lon) *
                      math.cos(latShanghai - lat))
    return d
