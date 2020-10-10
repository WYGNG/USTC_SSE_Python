from tkinter import * # Import tkinter
import tkinter.messagebox # Import tkinter.messagebox
from tkinter.filedialog import askopenfilename

# 导入模块
import matplotlib.pyplot as plt
# 构建数据
num_list = [20, 30, 15, 35]      # 纵坐标值
# 中文乱码处理
plt.rcParams["font.sans-serif"] = ["KaiTi"]
plt.rcParams['axes.unicode_minus'] = False
# 绘图
plt.bar(range(4),GDP,align = "center",color = "steelblue",alpha = 0.6)

# 添加y轴标签
plt.ylabel("出现次数")
# 设置Y轴的刻度范围
plt.ylim([0,100])

# 添加x轴刻度标签
plt.xticks(range(26),['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

# 添加标题
plt.title('各种字符出现频率')

# 为每个条形图添加数值标签
for x,y in enumerate(num_list):
    plt.text(x,y+300,'%s' %round(y,1),ha='center')# y+300 标签的坐标


# 显示图形
plt.show()  



def showResult():
    analyzeFile(filename.get())

def showtu():
    analyzeFile(filename.get())

def clearAll():
    text.delete(1.0,tkinter.END)

def analyzeFile(filename):
    try:
        infile = open(filename, "r") # 打开所选文件
    
        counts = 26 * [0] # 初始化计数器
        for line in infile:
            #按行读入
            countLetters(line.lower(), counts)
        
        # 显示结果
        for i in range(len(counts)):
            if counts[i] != 0:
                text.insert(END, chr(ord('a') + i) + " 出现 " + str(counts[i]) + ("次\n"))
    
        infile.close() # 关闭文件
    except IOError:
        tkinter.messagebox.showwarning("提示", "文件 " + filename + " 不存在")  

# 对所有字母计数 
def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
            
def openFile(): 
    filenameforReading = askopenfilename()# 返回文件名
    filename.set(filenameforReading)

#创建一个窗口
w = Tk() 
#设置一个标题
w.title("统计字母出现频率")

fr1 = Frame(w) # Hold four labels for displaying cards
fr1.pack()

scrollbar = Scrollbar(fr1)
scrollbar.pack(side = RIGHT, fill = Y)

text = Text(fr1, width = 80, height = 20, wrap = WORD, yscrollcommand = scrollbar.set, bg = "pink")
text.pack()

scrollbar.config(command = text.yview)

fr2 = Frame(w) # Hold four labels for displaying cards
fr2.pack()

Label(fr2, text = "输入文件名: ", bg = "green").pack(side = LEFT)
filename = StringVar()
Entry(fr2, width = 40, textvariable = filename, bg = "pink").pack(side = LEFT)
Button(fr2, text = "浏览", command = openFile, bg = "yellow").pack(side = LEFT)
Button(fr2, text = "清屏", command = clearAll, bg = "red").pack(side = LEFT)
Button(fr2, text = "显示结果", command = showResult, bg = "brown").pack(side = LEFT)
Button(fr2, text = "显示直方图", command = showtu, bg = "red").pack(side = LEFT)

w.mainloop() # Create an event loop

