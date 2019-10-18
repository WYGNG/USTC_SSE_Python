import tkinter as tk
window=tk.Tk()              #实例化一个窗口
window.title('my window')   #定义窗口标题
window.geometry('400x600')  #定义窗口大小
 
var=tk.StringVar()
l=tk.Label(window,bg='yellow',width=20,height=2,text='empty')
l.pack()
 
def print_selection():
    l.config(text='you have selected'+var.get())#让对象l显示括号里的内容
 
r1=tk.Radiobutton(window,text='option A',variable=var,value='A',command=print_selection)
r1.pack()                                  #将参数A传入var
r2=tk.Radiobutton(window,text='option B',variable=var,value='B',command=print_selection)
r2.pack()
r3=tk.Radiobutton(window,text='option C',variable=var,value='C',command=print_selection)
r3.pack()
 
window.mainloop()
