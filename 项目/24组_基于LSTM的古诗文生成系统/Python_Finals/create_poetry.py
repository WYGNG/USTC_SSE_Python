# -*- coding: utf-8 -*-
import tensorflow as tf
from train import model
from dispose_data import process_poetry
import numpy as np
from tkinter import *
from PIL import ImageTk

file_path = ['./data/wujue_all.txt', './data/wulv_all.txt', './data/qijue_all.txt', './data/qilv_all.txt']
model_path = ['./model/five_jue/', './model/five_lv/', './model/seven_jue/', './model/seven_lv/']


def get_type():
    # 獲取radiobutton的類型
    val = v.get()
    return val


def select_file(type):
    # 選擇文件路徑
    return file_path[type]


def select_model(type):
    # 選擇模型路徑
    return model_path[type]


def to_word(predict, vocabs):
    # 將模型輸出的概率轉化爲漢字
    predict = predict[0]
    predict /= np.sum(predict)
    sample = np.random.choice(np.arange(len(predict)), p=predict)
    if sample > len(vocabs):
        return vocabs[-1]
    else:
        return vocabs[sample]


def gen_poem(begin_word, file, models, poem_type):
    tf.reset_default_graph()
    n = [24, 48, 32, 64]
    List = ['5jue', '5lv', '7jue', '7lv']
    if poem_type in List:
        m = n[List.index(poem_type)]                                                # 选择对应的模型
    batch_size = 1
    print('loading model from %s' % models)
    vector, word_dic, words = process_poetry(file, poem_type)                       # 将对应数据集数字化
    input_data = tf.placeholder(tf.int32, [batch_size, None])
    loss, initial_state, last_state = model(input_data=input_data, words_len=len(
        words), rnn_size=128, num_layers=2, batch=batch_size)                       # 模型预测
    prediction = tf.nn.softmax(loss)                                                # 输出概率向量
    saver = tf.train.Saver(tf.global_variables())
    init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
    with tf.Session() as sess:
        sess.run(init_op)
        checkpoint = tf.train.latest_checkpoint(models)
        saver.restore(sess, checkpoint)                                              # 加载模型
        x = np.array([list(map(word_dic.get, 'B'))])                                 # 得到首字符的字典对应数字
        [predict, last_state_] = sess.run([prediction, last_state], feed_dict={input_data: x})
        begin_word_ = to_word(predict, words)                                        # 得到诗文首字
        word = begin_word or begin_word_                                             # 首字由用户输入或系统生成
        poem_ = ''
        i = 0
        while word != 'E':                                                           # 当预测出的字为尾字符时，停止预测
            poem_ += word
            i += 1
            if i > m:                                                                # 预测出的字数超出诗的范围时，停止预测
                break
            x = np.array([[word_dic[word]]])                                         # 将汉字数字化，作为测试集
            [predict, last_state_] = sess.run([prediction, last_state],
                                              feed_dict={input_data: x, initial_state: last_state_})
            word = to_word(predict, words)
        return poem_


def pretty_print_poem_5jue(word):
    # 輸出五言絕句
    begin_char = word
    poem_ = gen_poem(begin_char, select_file(get_type()), select_model(get_type()), '5jue')
    poem_sentences = poem_.split('。')
    p = '\n'
    for s in poem_sentences:
        if s != '' and len(s) > 10:
            s = str(s)+'。'+'\n'
            p = p + s
        label.config(text=p)


def pretty_print_poem_5lv(word):
    # 輸出五言律詩
    begin_char = word
    poem_ = gen_poem(begin_char, select_file(get_type()), select_model(get_type()), '5lv')
    poem_sentences = poem_.split('。')
    p = '\n'
    for s in poem_sentences:
        if s != '' and len(s) > 10:
            s = str(s)+'。'+'\n'
            p = p + s
        label.config(text=p)


def pretty_print_poem_7jue(word):
    # 輸出七言絕句
    begin_char = word
    poem_ = gen_poem(begin_char, select_file(get_type()), select_model(get_type()), '7jue')
    poem_sentences = poem_.split('。')
    p = '\n'
    for s in poem_sentences:
        if s != '' and len(s) > 14:
            s = str(s)+'。'+'\n'
            p = p + s
        label.config(text=p)


def pretty_print_poem_7lv(word):
    # 輸出七言律詩
    begin_char = word
    poem_ = gen_poem(begin_char, select_file(get_type()), select_model(get_type()), '7lv')
    poem_sentences = poem_.split('。')
    p = '\n'
    for s in poem_sentences:
        if s != '' and len(s) > 14:
            s = str(s)+'。'+'\n'
            p = p + s
        label.config(text=p)


def select_to_show():
    # 選擇輸出的詩文種類
    if get_type() == 0:
        pretty_print_poem_5jue(et.get())
    elif get_type() == 1:
        pretty_print_poem_5lv(et.get())
    elif get_type() == 2:
        pretty_print_poem_7jue(et.get())
    else:
        pretty_print_poem_7lv(et.get())


if __name__ == '__main__':
    window = Tk()
    window.title("古詩文生成系統")
    window.iconbitmap('./data/ustc.ico')
    pic = ImageTk.PhotoImage(file='./data/background.gif')
    frame1 = Frame(window)                                                     # 框架一 顯示詩文
    frame1.pack()
    label = Label(frame1, font=('方正楷体', 20), compound='center', image=pic)
    label.pack()
    frame2 = Frame(window, background='Wheat')                                 # 框架二 操作功能
    frame2.pack()
    Label(frame2, text="請輸入詩的首字:", height=2, width=20, font=('方正楷体', 10),
          background='Wheat', borderwidth=0).pack(side=LEFT)
    et = Entry(frame2, width=20, background='BlanchedAlmond')                  # 定义一个输入框，用于输入詩的開頭
    et.pack(side=LEFT)
    style = [('五絕', 0), ('五律', 1), ('七絕', 2), ('七律', 3)]                 # 定義一組radio button
    v = IntVar()
    for lan, var in style:
        Radiobutton(frame2, text=lan, value=var, command=get_type, variable=v,
                    font=('方正楷体', 10), background='Wheat', disabledforeground='Moccasin').pack(side=LEFT)
    Button(frame2, text="創作", command=select_to_show, height=2, width=10, font=('方正楷体', 10)
           , activebackground='Moccasin', background='BurlyWood',
           highlightbackground='BurlyWood', highlightcolor='BurlyWood').pack(side=RIGHT)  # 定义一个按钮
    window.mainloop()
