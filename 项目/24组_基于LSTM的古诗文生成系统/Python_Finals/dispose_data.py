# -*- coding: utf-8 -*-
import collections
import numpy as np


def process_poetry(file_name, poem_type):
    # 将诗文用数字表示
    n = [24, 48, 32, 64]
    m = [5, 5, 7, 7]
    List = ['5jue', '5lv', '7jue', '7lv']
    if poem_type in List:                                                   # 根据诗文类型，从文件中读取定长的文字
        p = n[List.index(poem_type)]
        q = m[List.index(poem_type)]
    poems = []
    with open(file_name, "r", encoding='utf-8', ) as f:
        for line in f.readlines():                                           # 逐行讀取
            title, content = line.strip().split(':')                         # title為符號':'之前的信息，content為符號':'后的詩文
            content = content.replace(' ', '')                               # 除去詩文中的空格
            if '_' in content or '(' in content or '（' in content or '《' in content or '[' in content or \
                    'B' in content or 'E' in content:                        # 當出現以上符號時，读取下一行
                continue
            if len(content) < q or len(content) > p:                         # 詩文長度小於7，或大於79時，读取下一行
                continue
            content = 'B' + content + 'E'                                    # 这两个值起到标记每一行起始和终止位置的作用
            poems.append(content)                                            # poem=['B君子坦荡荡E']
    all_words = []                                                           # 将每个字单独作为列表的一个元素存储,如：['B','君','子']
    for poem in poems:
        for word in poem:
            all_words.append(word)
    counter = collections.Counter(all_words)                                 # 记录每个字出现的次数
    words = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)   # 将出现次数最多的字排到最前。['荡','B','君','子','坦','E']
    words.append(' ')
    length = len(words)                                                      # 此为诗文中出现过的所有字的字数（不重复）
    word_dic = dict(zip(words, range(length)))                               # {'荡':0,'B':1,'君':2,'子':3,'坦':4,'E'"5}
    vector = [list(map(lambda word_: word_dic.get(word_, length), poem))     # 将诗文转为包含数字的二维向量，如[[1,2,3,4,0,0,5]]
              for poem in poems]
    return vector, word_dic, words                                           # 输出数字向量，字典和包含所有字的列表


def get_batch(batch_size, vector_, word_dic_):
    # 根据指定大小，输出训练数据
    n = len(vector_) // batch_size                                           # 循环次数
    x_batches = []
    y_batches = []
    for i in range(n):
        start_index = i * batch_size
        end_index = start_index + batch_size
        batches = vector_[start_index:end_index]                             # vector[64i:64(i+1)]：截取64行
        length = len(vector_[0])                                             # 为行长
        x_data = np.full((batch_size, length), word_dic_[' '], np.int32)     # 定义形状为(batch_size,length)的满矩阵
        for row, batch in enumerate(batches):
            x_data[row, :len(batch)] = batch                                 # 将batches中的值赋给x_data
        y_data = np.copy(x_data)
        y_data[:, :-1] = x_data[:, 1:]                                       # 将y_data中元素往前移一位，作为标签
        x_batches.append(x_data)                                             # (n,batch_size,length)
        y_batches.append(y_data)
    return x_batches, y_batches




