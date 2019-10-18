'''SA19225404 吴语港 作业二 第二题 解密'''

def main():
    #strip()方法用于移除字符串头尾指定的字符
    f1 = input("输入需解密文件名: ").strip()
    f2 = input("输入目标文件名: ").strip()

    #以只读方式打开输入文件 
    inputfile = open(f1, "r")
    #读取内容
    s = inputfile.read() 
    #string类tempS开头为空
    tempS = ""
    #遍历整个文件
    for i in range(len(s)):
    #chr()用一个范围在0～255整数作参数，返回一个对应的字符。ord的作用相反
        tempS += chr(ord(s[i]) - 5)
    #关闭输入文件
    inputfile.close()
    #以只写方式打开输出文件 
    outputfile = open(f2, "w")
    #结尾空
    print(tempS, file = outputfile, end = "") 
    print("完成") 
    #关闭输出文件
    outputfile.close() 

main()
