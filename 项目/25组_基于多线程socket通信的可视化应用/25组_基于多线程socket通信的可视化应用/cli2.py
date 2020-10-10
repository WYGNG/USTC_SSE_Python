# coding=gbk
from tkinter import *
from socket import *
from tkinter.filedialog import askopenfilename
import os
import re
import cv2
import numpy as np
from tkinter import messagebox
HOST = '127.0.0.1'
PORT = 22222
BUFSIZ = 1024
ADDR = (HOST, PORT)

class Repeat:
 def __init__(self):
  window=Tk()
  window.title("Repeat")
  self.text=Text(window,width=100,height=20)
  self.text.pack()
  self.Var=StringVar()
  frame1=Frame(window)
  frame1.pack()
  Label(frame1,text="Enter a message:").grid(row=1,column=1,sticky=W)
  e=Entry(frame1,textvariable=self.Var,width=40)
  e.grid(row=1,column=2)
  Button(frame1,text="Send",command=lambda:self.processSend(e)).grid(row=1,column=3)
  window.mainloop()

 def processSend(self,e):
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('������mode'.encode())
  data = tcpCliSock.recv(BUFSIZ).decode()
  data=e.get()
  self.text.insert(INSERT,'>')
  self.text.insert(INSERT,data)
  self.text.insert(INSERT,'\n')
  if not data:
   return
  tcpCliSock.send(data.encode())
  data = tcpCliSock.recv(BUFSIZ).decode()
  if not data:
   return
  self.text.insert(INSERT,data)
  self.text.insert(INSERT,'\n')
  e.delete(0,END)
  tcpCliSock.close()

class Transmit:
 def __init__(self):
  window=Tk()
  window.title("Transmit")
  self.text=Text(window,width=100,height=20)
  self.text.pack()
  self.Var=StringVar()
  frame1=Frame(window)
  frame1.pack()
  Label(frame1,text="Select the file:").grid(row=1,column=1,sticky=W)
  e=Entry(frame1,textvariable=self.Var,width=40)
  e.grid(row=1,column=2)
  Button(frame1,text="���",command=lambda:self.processBrowse(e)).grid(row=1,column=3)
  Button(frame1,text="ȷ�ϼ���",command=lambda:self.processEncrypt(e)).grid(row=1,column=4)
  frame2=Frame(window)
  frame2.pack()
  Button(frame2,text="ת�����ͻ���1",command=self.processTrans1).grid(row=1,column=1)
  Button(frame2,text="ת�����ͻ���3",command=self.processTrans3).grid(row=1,column=2)
  Button(frame2,text="ת�����ͻ���4",command=self.processTrans4).grid(row=1,column=3)
  frame3=Frame(window)
  frame3.pack()
  Button(frame3,text="�����ļ�",command=self.processRecv).grid(row=1,column=1)
  Button(frame3,text="�����ļ�",command=self.processDecrypt).grid(row=1,column=2)
  window.mainloop()

 def processBrowse(self,e):
  e.delete(0,END)
  m=askopenfilename()
  e.insert(0,m)
  
 def processEncrypt(self,e):
  filename=e.get()
  if os.path.exists(filename)==0: 
   messagebox.showinfo("Tip","The file is not exist!")
   return(0)
  f=open(filename,"r",encoding='utf-8')
  data=f.read()
  self.text.insert(INSERT,'>����ǰ�ļ�:\n')
  self.text.insert(INSERT,data)
  self.text.insert(INSERT,'\n')
  f.close()
  outfile=open(filename,"rb")
  list=[]
  while True:
   a=outfile.read(1)
   if not a:break
   list.append(a)
  for k in range(len(list)):
   if ord(list[k])+5>255:list[k]=ord(list[k])-250
   else:list[k]=ord(list[k])+5
  list=bytes(list)
  self.text.insert(INSERT,'>���ܺ��ļ�:\n')
  self.text.insert(INSERT,list)
  self.text.insert(INSERT,'\n')
  infile=open("jiami.txt","wb")
  infile.write(list)
  infile.close()
  outfile.close()
  self.text.insert(INSERT,'>���ܳɹ�,д��jiami.txt�ļ�\n')

 def processTrans1(self):
  outfile=open("jiami.txt","rb")
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('�����ļ�ת��mode1'.encode())
  data = tcpCliSock.recv(BUFSIZ).decode()
  data=outfile.read()
  if not data:
   return
  tcpCliSock.send(data)
  data = tcpCliSock.recv(BUFSIZ).decode()
  if data=='���ռ����ļ����':
   self.text.insert(INSERT,'>��������ļ����\n')
  tcpCliSock.close()
 
 def processTrans3(self):
  outfile=open("jiami.txt","rb")
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('�����ļ�ת��mode3'.encode())
  data = tcpCliSock.recv(BUFSIZ).decode()
  data=outfile.read()
  if not data:
   return
  tcpCliSock.send(data)
  data = tcpCliSock.recv(BUFSIZ).decode()
  if data=='���ռ����ļ����':
   self.text.insert(INSERT,'>��������ļ����\n')
  tcpCliSock.close()
  
 def processTrans4(self):
  outfile=open("jiami.txt","rb")
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('�����ļ�ת��mode4'.encode())
  data = tcpCliSock.recv(BUFSIZ).decode()
  data=outfile.read()
  if not data:
   return
  tcpCliSock.send(data)
  data = tcpCliSock.recv(BUFSIZ).decode()
  if data=='���ռ����ļ����':
   self.text.insert(INSERT,'>��������ļ����\n')
  tcpCliSock.close()
  
 def processRecv(self):
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('�����ļ�mode'.encode())
  data = tcpCliSock.recv(BUFSIZ)
  infile=open("recv2.txt","wb")
  infile.write(data)
  infile.close()
  tcpCliSock.send('success'.encode())
  tcpCliSock.close()
  self.text.insert(INSERT,'>���յ������ļ�������recv2.txt\n')

 def processDecrypt(self):
  outfile=open("recv2.txt","rb")
  list=[]
  while True:
   a=outfile.read(1)
   if not a:break
   list.append(a)
  for k in range(len(list)):
   if ord(list[k])-5<0:list[k]=ord(list[k])+250
   else:list[k]=ord(list[k])-5
  list=bytes(list)
  infile=open("jiemi.txt","wb")
  infile.write(list)
  infile.close()
  outfile.close()
  f=open("jiemi.txt","r",encoding='utf-8')
  data=f.read()
  self.text.insert(INSERT,'>���ܺ��ļ�:\n')
  self.text.insert(INSERT,data)
  self.text.insert(INSERT,'\n')

class Detection:
 def __init__(self):
  window=Tk()
  window.title("Detection")
  self.text=Text(window,width=100,height=20)
  self.text.pack()
  self.Var=StringVar()
  frame1=Frame(window)
  frame1.pack()
  Label(frame1,text="Select a picture:").grid(row=1,column=1,sticky=W)
  e=Entry(frame1,textvariable=self.Var,width=40)
  e.grid(row=1,column=2)
  Button(frame1,text="���",command=lambda:self.processBrowse(e)).grid(row=1,column=3)
  Button(frame1,text="ȷ�Ϸ���",command=lambda:self.processDelivery(e)).grid(row=1,column=4)
  Button(frame1,text="�����",command=self.processResult).grid(row=1,column=5)
  window.mainloop()
 
 def processBrowse(self,e):
  e.delete(0,END)
  m=askopenfilename()
  e.insert(0,m)

 def processDelivery(self,e):
  self.filename=e.get()
  if os.path.exists(self.filename)==0: 
   messagebox.showinfo("Tip","The file is not exist!")
   return 0
  elif re.search('\.jpg',self.filename) is None:
   messagebox.showinfo("Tip","The file is not picture.jpg!")
   return 
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('����ͼƬmode'.encode())
  if tcpCliSock.recv(BUFSIZ).decode()=='OK':
   self.text.insert(INSERT,'׼������ͼƬ\n')
  myfile = open(self.filename, 'rb')
  data = myfile.read()
  size = str(len(data))
  tcpCliSock.send(size.encode())
  rec = tcpCliSock.recv(BUFSIZ).decode()
  tcpCliSock.send(data)
  if tcpCliSock.recv(BUFSIZ).decode()=='OK':
   self.text.insert(INSERT,'����ͼƬ���\n')
  tcpCliSock.close()

 def processResult(self):
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('�������mode'.encode())
  rec = tcpCliSock.recv(BUFSIZ).decode()
  if rec=='No face':
   tcpCliSock.close()
   messagebox.showinfo("Tip","No face in the picture!")
  else:
   list=rec.split(',')
   tcpCliSock.close()
   img = cv2.imdecode(np.fromfile(self.filename,dtype=np.uint8),-1)
   vis = img.copy()
   window=Tk()
   window.title("Information")
   canvas=Canvas(window,width=400,height=400,bg='white')
   canvas.pack()
   canvas.create_text(200,100,text=''.join(['�Ա�',list[0]]))
   canvas.create_text(200,200,text=''.join(['Ԥ�����䣺',list[1]]))
   canvas.create_text(200,300,text=''.join(['��ֵ�÷֣�',list[2]]))
   cv2.rectangle(vis, (int(list[6]), int(list[4])), (int(list[6])+int(list[3]), int(list[4])+int(list[5])),(0, 255, 0), 2)
   cv2.imshow("Image", vis)
   cv2.waitKey (0)

class Analyze:
 def __init__(self):
  window=Tk()
  window.title("Analyze")
  self.text=Text(window,width=100,height=20)
  self.text.pack()
  self.Var=StringVar()
  frame1=Frame(window)
  frame1.pack()
  Label(frame1,text="Select a file:").grid(row=1,column=1,sticky=W)
  e=Entry(frame1,textvariable=self.Var,width=40)
  e.grid(row=1,column=2)
  Button(frame1,text="���",command=lambda:self.processBrowse(e)).grid(row=1,column=3)
  Button(frame1,text="ȷ�Ϸ���",command=lambda:self.processDelivery(e)).grid(row=1,column=4)
  Button(frame1,text="���ݷ���",command=self.processAnalyze).grid(row=1,column=5)
  frame2=Frame(window)
  frame2.pack()
  Button(frame2,text="����ͼ",command=self.processPic1).grid(row=1,column=1)
  Button(frame2,text="��״ͼ",command=self.processPic2).grid(row=1,column=2)
  Button(frame2,text="��״ͼ",command=self.processPic3).grid(row=1,column=3)
  Button(frame2,text="ɢ��ͼ",command=self.processPic4).grid(row=1,column=4)
  Button(frame2,text="����ͼ",command=self.processPic5).grid(row=1,column=5)
  window.mainloop()

 def processBrowse(self,e):
  e.delete(0,END)
  m=askopenfilename()
  e.insert(0,m)

 def processDelivery(self,e):
  self.filename=e.get()
  if os.path.exists(self.filename)==0: 
   messagebox.showinfo("Tip","The file is not exist!")
   return 0
  elif re.search('\.csv',self.filename) is None:
   messagebox.showinfo("Tip","The file is not file.csv!")
   return 
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('����csv�ļ�mode'.encode())
  if tcpCliSock.recv(BUFSIZ).decode()=='OK':
   self.text.insert(INSERT,'׼������csv�ļ�\n')
  myfile = open(self.filename, 'rb')
  data = myfile.read()
  size = str(len(data))
  tcpCliSock.send(size.encode())
  rec = tcpCliSock.recv(BUFSIZ).decode()
  tcpCliSock.send(data)
  if tcpCliSock.recv(BUFSIZ).decode()=='OK':
   self.text.insert(INSERT,'����csv�ļ����\n')
  tcpCliSock.close()

 def processAnalyze(self):
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('���ݷ���mode'.encode())
  rec=tcpCliSock.recv(BUFSIZ).decode()
  if rec=='OK':
   messagebox.showinfo("Tip","Data analysis complete!")
  else:messagebox.showinfo("Tip","An unexpected error occurred!!")
  tcpCliSock.close()

 def processPic1(self):
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('����ͼmode'.encode())
  size= tcpCliSock.recv(BUFSIZ).decode()
  tcpCliSock.send('OK'.encode())
  size=int(size)
  data = tcpCliSock.recv(size)
  myfile = open('heatmap.jpg', 'wb')
  myfile.write(data)
  myfile.close()
  tcpCliSock.send('OK'.encode())
  tcpCliSock.close()
  img = cv2.imread("heatmap.jpg")
  cv2.imshow("Image", img)
  cv2.waitKey (0)

 def processPic2(self):
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('��״ͼmode'.encode())
  size= tcpCliSock.recv(BUFSIZ).decode()
  tcpCliSock.send('OK'.encode())
  size=int(size)
  data = tcpCliSock.recv(size)
  myfile = open('hist.jpg', 'wb')
  myfile.write(data)
  myfile.close()
  tcpCliSock.send('OK'.encode())
  tcpCliSock.close()
  img = cv2.imread("hist.jpg")
  cv2.imshow("Image", img)
  cv2.waitKey (0)
 
 def processPic3(self):
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('��״ͼmode'.encode())
  size= tcpCliSock.recv(BUFSIZ).decode()
  tcpCliSock.send('OK'.encode())
  size=int(size)
  data = tcpCliSock.recv(size)
  myfile = open('pie.jpg', 'wb')
  myfile.write(data)
  myfile.close()
  tcpCliSock.send('OK'.encode())
  tcpCliSock.close()
  img = cv2.imread("pie.jpg")
  cv2.imshow("Image", img)
  cv2.waitKey (0)

 def processPic4(self):
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('ɢ��ͼmode'.encode())
  size= tcpCliSock.recv(BUFSIZ).decode()
  tcpCliSock.send('OK'.encode())
  size=int(size)
  data = tcpCliSock.recv(size)
  myfile = open('distplot.jpg', 'wb')
  myfile.write(data)
  myfile.close()
  tcpCliSock.send('OK'.encode())
  tcpCliSock.close()
  img = cv2.imread("distplot.jpg")
  cv2.imshow("Image", img)
  cv2.waitKey (0)

 def processPic5(self):
  tcpCliSock = socket(AF_INET, SOCK_STREAM)
  tcpCliSock.connect(ADDR)
  tcpCliSock.send('����mode'.encode())
  count= tcpCliSock.recv(BUFSIZ).decode()
  tcpCliSock.send('OK'.encode())
  count=int(count)
  for i in range(count):
   size= tcpCliSock.recv(BUFSIZ).decode()
   tcpCliSock.send('OK'.encode())
   size=int(size)
   data = tcpCliSock.recv(size)
   myfile = open('�ͻ���2����'+str(i)+'.jpg', 'wb')
   myfile.write(data)
   myfile.close()
   tcpCliSock.send('OK'.encode())
  for i in range(count):
   img = cv2.imdecode(np.fromfile('�ͻ���2����'+str(i)+'.jpg',dtype=np.uint8),-1)
   cv2.imshow("Image", img)
   cv2.waitKey (0)
  tcpCliSock.close()

class Cli:
 def __init__(self):
  window=Tk()
  window.title("Client2")
  self.text=Text(window,width=100,height=20)
  self.text.pack()
  frame1=Frame(window)
  frame1.pack()
  Button(frame1,text="������ģʽ",command=self.processRepeat).grid(row=1,column=1)
  Button(frame1,text="�ļ�����ת��",command=self.processTransmit).grid(row=1,column=2)
  Button(frame1,text="�������",command=self.processDetection).grid(row=1,column=3)
  Button(frame1,text="���ݷ���",command=self.processAnalyze).grid(row=1,column=4)
  window.mainloop()

 def processRepeat(self): 
  self.text.insert(INSERT,'������ģʽ����\n')
  Repeat()

 def processTransmit(self):
  self.text.insert(INSERT,'�ļ�����ת������\n')
  Transmit()

 def processDetection(self):
  self.text.insert(INSERT,'������⿪��\n')
  Detection()

 def processAnalyze(self):
  self.text.insert(INSERT,'���ݷ�������\n')
  Analyze()

Cli()