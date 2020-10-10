# Prompt the user to enter a positive integer
number = eval(input("Enter a positive integer: "))
    
# Find all the smallest factors of the integer
print("The factors for " + str(number) + " is ", end = "")
factor = 2
while factor <= number:
    if number % factor == 0:
        number = number / factor
        print(factor, end = " ")
    else:
        factor += 1