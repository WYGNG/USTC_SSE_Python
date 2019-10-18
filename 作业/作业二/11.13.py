'''SA19225404 吴语港 作业二 第一题'''

def locateLargest():
    #输入行数
    rows = eval(input("Enter the number of rows in the list: "))
    #输入行，并寻找最大值并记录位置
    for i in range(rows):#按行循环
        items = input("Enter a row: ").strip().split()#对输入的串去除空格并切片
        list = [ eval(x) for x in items ] #字符类型转换成数值并排成列表
        for j in range(len(list)):#按列循环
            if i == 0 and j == 0:#初始化最大值
                m = list[0]
            if list[j]>m:
                m = list[j]#寻找最大值
                a,b = i,j#记录最大值位置
    return [a,b]#返回最大值位置


def main():
    print("The location of the largest element is at",locateLargest())
main()
