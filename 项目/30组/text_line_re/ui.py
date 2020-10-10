import tkinter as tk
from tkinter import filedialog,ttk
from PIL import Image,ImageTk
window = tk.Tk()
import os

# coding=utf-8
from CNN_seq2seqv2_1_atten import CRNN
from keras import backend as K
from keras.layers import Conv2D, Bidirectional, LSTM, BatchNormalization, Input, Reshape, Dense, Activation, Dropout, \
    AveragePooling2D, ZeroPadding2D, Permute, Flatten, Lambda
from keras import Model
from keras.optimizers import Adam
from keras.layers.merge import concatenate
from keras.regularizers import l2
from keras.activations import relu
import tensorflow as tf
from keras.layers.wrappers import TimeDistributed
from keras.utils.vis_utils import plot_model
import numpy as np
from PIL import Image
from char_dict import char_dict, chars
from keras.callbacks import EarlyStopping, ModelCheckpoint, LearningRateScheduler, TensorBoard
from keras.utils.np_utils import to_categorical
import heapq


def ctc_lambda_func(args):
    y_pred, labels, input_length, label_length = args
    return K.ctc_batch_cost(labels, y_pred, input_length, label_length)


def gen_model(img_h, nclass):
    input = Input(shape=(img_h, None, 1), name='input_img')
    y_pred = CRNN(input, nclass)

    basemodel = Model(inputs=input, outputs=y_pred)

    labels = Input(name='the_labels', shape=[None], dtype='float32')
    input_length = Input(name='input_length', shape=[1], dtype='int64')
    label_length = Input(name='label_length', shape=[1], dtype='int64')

    loss_out = Lambda(ctc_lambda_func, output_shape=(1,), name='ctc')([y_pred, labels, input_length, label_length])

    model = Model(inputs=[input, labels, input_length, label_length], outputs=loss_out)
    model.compile(loss={'ctc': lambda y_true, y_pred: y_pred}, optimizer='adam', metrics=['accuracy'])

    return basemodel, model


basemodel, model = gen_model(32, 3757)

print('-----------Start training-----------')
model.summary()
model.load_weights('./models/weights_crnnseq2seq-05-val_loss-0.18-val-acc-0.991.h5')
import os
def files_walk(path):
    for r, _, f in os.walk(path):
        return r, f








def open_file():
    '''
    打开文件
    :return:
    '''
    global file_path
    global file_text
    file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
    print('打开文件：', file_path)
    if file_path is not None:
        img_name = file_path
        img = Image.open(img_name)
        render = ImageTk.PhotoImage(img)
        label_img.config(image=render)
        label_img.image=render
        img = img.convert('L')
        img = img.resize((int(img.width * 32 / img.height), 32), Image.ANTIALIAS)
        img_np = np.array(img) / 255.0 - 0.5
        img_np = np.expand_dims(img_np, 0)
        img_np = np.expand_dims(img_np, -1)
        label = img_name.split('.')[-2]
        label = label.split('/')[-1]
        #
        from stringmatch import match

        pred = basemodel.predict(img_np)
        predlabels =''
        name5 = []
        poss5 = []
        for i, y in enumerate(pred[:]):
            for topk in range(5):
                ychars = y.argmax(-1)
                name = ''
                pos = []
                poss = []
                for pi, ci in enumerate(ychars[:]):
                    if ci < 3756:
                        pos.append(y[pi, ci])
                        y[pi, ci] = 0
                        name += chars[ci]
                    else:
                        name += '-'
                        pos.append(y[pi, ci])
                        y[pi, ci] = 0
                name5.append(name)
                poss5.append(pos)
                name += '-'
                pos.append(pos[-1])
                nname = ''
                for ii, ci in enumerate(name):
                    if ii < len(name) - 1:
                        if name[ii] != name[ii + 1] and name[ii] != '-':
                            nname += name[ii]


                if topk==0:
                    predlabels=nname

        print(name5)
        print(poss5)
        a, b, c = match(name5[0].replace('-',''), label)

        print(c)
        text1.delete(0.0,tk.END)
        if len(c)==0:
            text1.insert('insert',predlabels+'\n' '正确')
        else:
            text1.insert('insert',predlabels+'\n' +str(c))

        value5=[]
        for i5 in range(5):
            value=[]
            for ll in range(len(name5[0])):
                value.append(name5[i5][ll])
                value.append('%.3f'%poss5[i5][ll])
            value5.append(value)

        valnp = np.array(value5)
        value5 =valnp.T.tolist()
        items = treeview.get_children()

        [treeview.delete(item) for item in items]
        for ii,vv in enumerate(value5):
            treeview.insert('',ii,values=vv)
    # window.update()
    # window.update_idletasks()









window.title('文本行识别-中科大软院')

window.geometry('800x600')

img = Image.open('./1.jpg')
render = ImageTk.PhotoImage(img)

label_img = tk.Label(window, image = render)

text1 = tk.Text(window, width=50, height=2, bg='white', font=('Arial', 12))


label_img.pack()

text1.pack()
bt1 = tk.Button(window, text='打开文件', width=15, height=2, command=open_file)
bt1.pack()

columns = ["1","2","3","4","5"]
treeview = ttk.Treeview(window, height=18, show="headings", columns=columns)  # 表格


for cl in columns:
    treeview.column(cl, width=40, anchor='center')
    treeview.heading(cl, text=cl)  # 显示表头



treeview.pack(side=tk.TOP, fill=tk.BOTH)
window.mainloop()
