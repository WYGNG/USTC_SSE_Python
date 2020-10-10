count = 1
for i in range(100, 1001):
    if i % 5 == 0 and i % 6 == 0:
        if count % 10 != 0:
            print(i, end = " ")
        else:
            print(i)    
        
        count += 1