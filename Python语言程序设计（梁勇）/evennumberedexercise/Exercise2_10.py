v, a = eval(input("Enter speed and acceleration: "))

length = v * v / (2 * a)
    
print("The minimum runway length for this airplane is " + str(length) + " meters")