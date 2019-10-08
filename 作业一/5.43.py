count = 0;  #计数
for i in range(1,7,1):  #第一个数取1到7
    j = i + 1
    while  j <= 7:      #第一个数取大于第一个数到7
        print(i,j) 
        j = j + 1
        count = count + 1
print("The total number of all combinations is",count)

