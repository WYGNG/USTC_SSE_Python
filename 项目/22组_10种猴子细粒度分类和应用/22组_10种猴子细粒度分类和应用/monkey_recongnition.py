import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from PIL import Image, ImageTk

import matplotlib.pyplot as plt
from cnn_model import *


class FileWindow:
    def __init__(self):
        # 加载模型和标签
        self.model = train_model().load_model()
        self.labels = train_model().labels

        self.ratio = 1  # 图像缩放比例

        self.window = tk.Tk()
        self.filename = tk.StringVar()  # 打开的文件名
        self.window.title("猴子类型识别")
        self.window.geometry('800x600')
        self.newtk_image = ImageTk.PhotoImage(file="/Users/cuiyonghu/Desktop/monkey_class/logo.png")
        self.newtarget = tk.Label(self.window, image = self.newtk_image,bg="white",width=200,height=100)
        self.label_filename = tk.Label(self.window, text='Load a File')
        self.entry_filename = tk.Entry(self.window, show=None, textvariable=self.filename)
        self.button_Browse = tk.Button(self.window, text='Browse', command=self.hitBrowse)
        self.button_Result = tk.Button(self.window, text='show result', command=self.hitResult)
        self.button_shrink = tk.Button(self.window, text='Shrink', command=self.hitShrink)
        self.button_enlarge = tk.Button(self.window, text='Enlarge', command=self.hitEnlarge)
        self.text_empty = tk.Label(self.window, text="\r\n\n")
        self.text_intro = tk.Label(self.window, text='系统简介\r\n')
        self.text_content = tk.Label(self.window, text='本项目实现了一个可以对十种特定的\r\n'
                                                       '猴子进行分类识别的系统，并设计了\r\n'
                                                       '相应的界面操作程序用户可以通过按\r\n'
                                                       '键选择输入含有特定的猴子类别的图\r\n'
                                                       '片，最终系统会弹出一个提示框告知\r\n'
                                                       '用户输入图片中猴子的类别信息。')
        self.tk_image = None

        # self.target = tk.Label(self.window, image=self.tk_image, relief='sunken', bg="gray")
        self.target = tk.Label(self.window, image=self.tk_image,  bg="white")

        # self.label_filename.place(x=50, y=660)
        # self.entry_filename.place(x=150, y=660)
        # self.button_Browse.place(x=350, y=660)
        # self.button_Result.place(x=420, y=660)
        # self.button_shrink.place(x=520, y=660)
        # self.button_enlarge.place(x=580, y=660)
        # self.target.pack(fill='none', padx=8, pady=8, side='top', anchor='s', expand=False)

        # self.label_filename.pack(padx=8, pady=8, side='left', anchor='n')
        # self.entry_filename.pack(padx=8, pady=8, side='left', anchor='n')
        # self.button_Browse.pack(padx=8, pady=8, side='left', anchor='n')
        # self.button_Result.pack(padx=8, pady=8, side='left', anchor='n')
        # self.button_shrink.pack(padx=8, pady=8, side='left', anchor='n')
        # self.button_enlarge.pack(padx=8, pady=8, side='left', anchor='n')
        # self.target.pack(fill='both', padx=8, pady=8, side='bottom', anchor='w', expand=0 ,before=self.label_filename)

        # padx=5
        # pady=5
        # self.label_filename.grid(padx=padx, pady=pady,row=0, column=0)
        # self.entry_filename.grid(padx=padx, pady=pady,row=1, column=0)
        # self.button_Browse.grid(padx=padx, pady=pady,row=2, column=0)
        # self.button_Result.grid(padx=padx, pady=pady,row=3, column=0)
        # self.button_shrink.grid(padx=padx, pady=pady,row=4, column=0)
        # self.button_enlarge.grid(padx=padx, pady=pady,row=5, column=0)
        self.newtarget.grid(row=0,column=0)
        self.label_filename.grid(row=1, column=0)
        self.entry_filename.grid(row=2, column=0)
        self.button_Browse.grid(ipadx=40, row=3, column=0)
        self.button_Result.grid(ipadx=30,row=4, column=0)
        self.button_shrink.grid(ipadx=43,row=5, column=0)
        self.button_enlarge.grid(ipadx=40,row=6, column=0)
        self.text_empty.grid(rowspan=5, column=0)
        self.text_intro.grid(row=11, column=0)
        self.text_content.grid(row=12,rowspan=100, column=0)
        self.target.grid(padx=8, pady=8,row=0, rowspan=1000, column=1)

        self.window.mainloop()

    def hitBrowse(self):
        default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
        name = tk.filedialog.askopenfilename(title=u"选择文件",
                                             initialdir=(os.path.expanduser(default_dir)))
        self.filename.set(name)
        # 加载图片
        filepath = self.filename.get()
        self.tk_image = Image.open(filepath)
        w, h = self.tk_image.size
        ratio = h / w
        if w > h:
            w = 600
            h = ratio * w
        else:
            h = 600
            w = h / ratio
        self.tk_image = self.tk_image.resize([int(w), int(h)])

        # 加载照片
        image_file = ImageTk.PhotoImage(self.tk_image)
        self.target.config(image=image_file)
        self.target.image = image_file

    def hitShrink(self):
        if self.tk_image == None:
            tk.messagebox.showinfo(title='Warning', message='The Image not Exist')
            return
        if self.ratio>0.1:
            self.ratio -= 0.1
        w, h = self.tk_image.size
        image_file = ImageTk.PhotoImage(self.tk_image.resize([int(self.ratio * w), int(self.ratio * h)]))
        self.target.config(image=image_file)
        self.target.image = image_file

    def hitEnlarge(self):
        if self.tk_image == None:
            tk.messagebox.showinfo(title='Warning', message='The Image not Exist')
            return
        self.ratio += 0.1
        w, h = self.tk_image.size
        image_file = ImageTk.PhotoImage(self.tk_image.resize([int(self.ratio * w), int(self.ratio * h)]))
        self.target.config(image=image_file)
        self.target.image = image_file

    def hitResult(self):
        # 打开文件
        if not os.path.exists(self.filename.get()):
            tk.messagebox.showinfo(title='Warning', message='The File not Exist')
            return
        filepath = self.filename.get()
        img = Image.open(filepath)

        # 预处理
        image = img.resize([224, 224])
        images = []
        image = np.asarray(image)
        images.append(image)
        images = np.array(images)
        # 预测
        result_labels = train_model().predict(images, self.model)
        # print(result_labels.argmax(axis=1))

        message = train_model().labels[result_labels.argmax(axis=1)[0]]
        message = '第{}类:'.format(result_labels.argmax(axis=1)[0]) + message
        tk.messagebox.showinfo(title='猴子类别', message=message)


if __name__ == '__main__':
    FileWindow()
