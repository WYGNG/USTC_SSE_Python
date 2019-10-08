import time

numberOfSeconds = eval(input("Enter the number of second: "))
    
while numberOfSeconds > 0:
    time.sleep(1)
    if numberOfSeconds > 1:
        print(str(numberOfSeconds)+ " seconds remaining")      
    else:
        print("1 second remaining")
    numberOfSeconds -= 1
    
print("Stopped")