import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

import train
import settings
import eval

class Occur:
    def __init__(self):
        window = Tk()
        window.title("Image Transferation")
        self.Var1 = StringVar()
        self.Var2 = StringVar()
        self.Var3 = StringVar()
        self.Var4 = StringVar()
        self.Var5 = StringVar()

        self.canvas = Canvas(window, width=800, height=555, bg='white')
        self.canvas.pack()
        frame1 = Frame(window)
        frame1.pack()

        frame2 = Frame(window)
        frame2.pack()

        frame3 = Frame(window)
        frame3.pack()

        #filename = './images/school.png'
        #load = Image.open(filename)
        #load = load.resize((800, 50))
        #render = ImageTk.PhotoImage(load)
        #img = Label(self.canvas2, image=render)
        #img.image = render
        #img.place(x=0, y=0)

        filename = './images/school.png'
        load = Image.open(filename)
        load = load.resize((600, 50))
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=100, y=0)

        filename = './images/institute.png'
        load = Image.open(filename)
        load = load.resize((100, 50))
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=700, y=500)

        self.canvas.create_text(750, 470, text='By:\n刁海勇 郝日威\n李静雯 李朝伟')

        Label(frame1, text="Enter the path of the content image:").grid(row=1, column=1, sticky=W)
        e1 = Entry(frame1, textvariable=self.Var1, width=40)
        e1.grid(row=1, column=2)
        Button(frame1, text="Browse", command=lambda: self.processBrowse(e1)).grid(row=1, column=3)
        Button(frame1, text="Show Image", command=self.showImg1).grid(row=1, column=4)
        Label(frame1, text="Enter the path of the style image:").grid(row=2, column=1, sticky=W)

        e2 = Entry(frame1, textvariable=self.Var2, width=40)
        e2.grid(row=2, column=2)
        Button(frame1, text="Browse", command=lambda: self.processBrowse(e2)).grid(row=2, column=3)
        Button(frame1, text="Show Image", command=self.showImg2).grid(row=2, column=4)

        e3 = Entry(frame2, textvariable = self.Var3, width=5)
        e3.grid(row=1,column=1)
        Button(frame2, text="SetAlpha", command=self.setAlpha).grid(row=1,column=2)

        e4 = Entry(frame2, textvariable=self.Var4, width=5)
        e4.grid(row=1, column=3)
        Button(frame2, text="SetBeta", command=self.setBeta).grid(row=1, column=4)

        e5 = Entry(frame2, textvariable=self.Var5, width=5)
        e5.grid(row=1, column=5)
        Button(frame2, text="SetStep", command=self.setStep).grid(row=1, column=6)

        Button(frame2, text='Merge', command=self.merge).grid(row=2, column = 3)

        Button(frame3, text='Fast Image Transferation', command=self.reply).grid(row=2,column=1)

        window.mainloop()

    def processBrowse(self, e):
        e.delete(0, END)
        m = askopenfilename()
        e.insert(0, m)

    def showImg1(self):
        filename = self.Var1.get()
        settings.CONTENT_IMAGE = filename

        #eval.img = settings.CONTENT_IMAGE
        load = Image.open(filename)
        load = load.resize((400, 250))
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.place(x=0, y=50)

    def showImg2(self):
        filename = self.Var2.get()
        settings.STYLE_IMAGE = filename
        load = Image.open(filename)
        load = load.resize((400, 250))
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.place(x=400, y=50)

    def merge(self):
        print("Merging...")

        train.train()

        filename = 'images/output.jpg'
        load = Image.open(filename)
        load = load.resize((400, 250))
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.place(x=200, y=305)

    def setAlpha(self):
        settings.ALPHA = float(self.Var3.get())
        print("ALPHA:",settings.ALPHA)

    def setBeta(self):
        settings.BETA = float(self.Var4.get())
        print("BETA：",settings.BETA)

    def setStep(self):
        settings.TRAIN_STEPS = int(self.Var5.get())
        print("TRAIN_STEPS:",settings.TRAIN_STEPS)

    def reply(self):
        class Occur1:
            def __init__(self):
                window2 = Toplevel()#使用顶级窗口而不是根窗口
                window2.title("Fast Image Transferation")
                self.canvas2 = Canvas(window2, width=800, height=505, bg='white')
                self.canvas2.pack()

                frame4 = Frame(window2)
                frame4.pack()

                self.Var6 = IntVar()
                #self.v6.set(1)

                #filename='E:\Python\myPython\image style transfer\nerual_style_change-master\images\school.png'
                #load = Image.open(filename)
                #load = load.resize((700, 100))
                #render = ImageTk.PhotoImage(load)

                filename = './images/school.png'
                load = Image.open(filename)
                load = load.resize((600, 50))
                render = ImageTk.PhotoImage(load)
                img = Label(self.canvas2, image=render)
                img.image = render
                img.place(x=100, y=0)

                filename = './images/institute.png'
                load = Image.open(filename)
                load = load.resize((100, 50))
                render = ImageTk.PhotoImage(load)
                img = Label(self.canvas2, image=render)
                img.image = render
                img.place(x=700, y=450)

                self.canvas2.create_text(750, 420, text='By:\n刁海勇 郝日威\n李静雯 李朝伟')

                rb1 = Radiobutton(frame4, text="Model1", variable=self.Var6, value=1, command=self.selectModel)
                rb2 = Radiobutton(frame4, text="Model2", variable=self.Var6, value=2, command=self.selectModel)
                rb3 = Radiobutton(frame4, text="Model3", variable=self.Var6, value=3, command=self.selectModel)
                rb4 = Radiobutton(frame4, text="Model4", variable=self.Var6, value=4, command=self.selectModel)
                rb1.grid(row=1, column=1)
                rb2.grid(row=1, column=2)
                rb3.grid(row=1, column=3)
                rb4.grid(row=1, column=4)

                Button(frame4, text="Result", command=self.fastTransferation).grid(row=2, column=2)

                window2.mainloop()

            def selectModel(self):
                num=self.Var6.get()
                #print(num)
                if num==1:
                    eval.FLAGS.model_file = './model/denoised_starry.ckpt-done'
                elif num==2:
                    eval.FLAGS.model_file = './model/cubist.ckpt-done'
                    #print(eval.style_model)
                elif num==3:
                    eval.FLAGS.model_file = './model/feathers.ckpt-done'
                elif num==4:
                    eval.FLAGS.model_file = './model/wave.ckpt-done'

            #def selectModel2(self):
                #print(self.Var6.get())
                #eval.style_model = './model/cubist.ckpt-done'

            #def selectModel3(self):
                #print(self.Var6.get())
                #eval.style_model = './model/feathers.ckpt-done'

            #def selectModel4(self):
                #print(self.Var6.get())
                #eval.style_model = './model/wave.ckpt-done'

            def fastTransferation(self):

                eval.FLAGS.image_file = settings.CONTENT_IMAGE

                eval.test(eval.img)

                filename = 'generated/res.jpg'
                load = Image.open(filename)
                load = load.resize((400, 250))
                render = ImageTk.PhotoImage(load)

                img = Label(self.canvas2, image=render)
                img.image = render
                img.place(x=200, y=125)


        Occur1()

Occur()

